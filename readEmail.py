import imaplib
import email
from email.header import decode_header
from email_reply_parser import EmailReplyParser
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


obras = {
    "vale": {
        "barragemObra": [18, None],
        "barragemCNPJ": [1, 18], 
        "operacao": [38, None], 
        "infra":[23, None], 
        "remanescente": [25, None]
    },
    "publica": {
        "cnpj":[1, [1,3]],
        "oficina":[1,23],
        "goinia":[1,35],
        "trilha_mirante":[20,None],
        "capanema": [21,None],
        "sebrae": [29, None],
        "pq_mirante":[34, None],
        "pq_linear":[37,None]
    },
    "consorcio":{
        "candeias":[27, None],
        "ji-parana":[28,None],
        "tapa_buraco":[31,None],
        "rio_da_vala":[33,None],
        "rio_caete":[35,None]
    }
}


EMAIL = os.getenv("EMAIL_USER")
SENHA = os.getenv("EMAIL_PSWD")
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, SENHA)

def decode_cabecalho(txt_code):
    if not txt_code:
        return ""
    partes = decode_header(txt_code)
    result = []

    for texto, enconding in partes:
        if isinstance(texto, bytes):
            enconding = enconding if enconding else "utf-8"
            try:
                result.append(texto.decode(enconding))
            except UnicodeDecodeError:
                result.append(texto.decode("latin1", errors="replace"))
        else:
            result.append(texto)
    return "".join(result)

def catch_email():
    mail.select("inbox")
    status, mensagens = mail.search(None, "UNSEEN")
    ids = mensagens[0].split()
    for i in ids:
        status, dados = mail.fetch(i, "(BODY.PEEK[])")
        raw_email = dados[0][1]
        mensagem = email.message_from_bytes(raw_email)
        corpo = ""
        if mensagem.is_multipart():
            for part in mensagem.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    corpo = part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8")
                    break
        else:
            corpo = mensagem.get_payload(decode=True).decode(mensagem.get_content_charset() or "utf-8")

        corpo = EmailReplyParser.parse_reply(corpo)
        subject, enconding = decode_header(mensagem["subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(enconding or "utf-8")
        remetente = decode_cabecalho(mensagem["from"])
        assunto = decode_cabecalho(mensagem["subject"])
    return remetente, assunto, corpo


#def verificarObra(corpo):
    #for key, value in obras.items():
        

remetente, assunto,corpo = catch_email()

print(f'Email: {remetente}')
print(f'Assunto: {assunto}')
#print(f"Corpo: {corpo}")

#print(f"{obras['vale']['remanescente'][0]}")
mail.logout()
