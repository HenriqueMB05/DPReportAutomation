import imaplib
import email
from email.header import decode_header
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

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
        status, dados = mail.fetch(i, "(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT)])")
        raw_email = dados[0][1]
        mensagem = email.message_from_bytes(raw_email)
        subject, enconding = decode_header(mensagem["subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(enconding or "utf-8")
        remetente = decode_cabecalho(mensagem["from"])
        assunto = decode_cabecalho(mensagem["subject"])
    return remetente, assunto

remetente, assunto = catch_email()

print(f'Email: {remetente}')
print(f'Assunto: {assunto}')

mail.logout()
