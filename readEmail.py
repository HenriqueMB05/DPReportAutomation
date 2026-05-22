import imaplib
import email
from email.header import decode_header
from email_reply_parser import EmailReplyParser
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


class Email:
    def __init__(self):
        self.obras = {
            "vale": {
                "barragem obra": ["18", None],
                "barragem_cnpj": ["1", "18"], 
                "operacao": ["38", None], 
                "infra":["23", None], 
                "remanescente": ["25", None]
            },
            "publica": {
                "cnpj":["1", "1,3"],
                "oficina":["1","23"],
                "goinia":["1","35"],
                "trilha_mirante":["20",None],
                "capanema": ["21",None],
                "sebrae": ["29", None],
                "pq_mirante":["34", None],
                "pq_linear":["37",None]
            },
            "consorcio":{
                "candeias":["27", None],
                "ji-parana":["28",None],
                "tapa_buraco":["31",None],
                "rio_da_vala":["33",None],
                "rio_caete":["35",None]
            }
        }


        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PSWD")
        self.mail = None

    def conectar(self):
        self.mail = impaplib.IMAP4_SLL("imap.gmail.com")
        self.mail.login(self.email_user, self.email_password)
        self.mail.select("inbox")

    def desconectar(self):
        if self.mail:
            self.mail.logout()

    def _decode_cabecalho(self, email):
        if not email:
            return ""
        partes = decode_header(email)
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

    def catch_emails(self):
        status, mensagens = self.mail.search(None, "UNSEEN")
        ids = mensagens[0].split()

        lista_emails = []

        for i in ids:
            status, dados = mail.fetch(i, "(BODY.PEEK[])")
            raw_email = dados[0][1]
            mensagem = email.message_from_bytes(raw_email)
            corpo = ""
            if mensagem.is_multipart():
                for part in mensagem.walobra_email():
                    content_type = part.get_content_type()
                    if content_type == "text/plain":
                        corpo = part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8")
                        breaobra_email
            else:
                corpo = mensagem.get_payload(decode=True).decode(mensagem.get_content_charset() or "utf-8")

            corpo = EmailReplyParser.parse_reply(corpo)
            subject, enconding = decode_header(mensagem["subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(enconding or "utf-8")
            remetente = decode_cabecalho(mensagem["from"])
            assunto = decode_cabecalho(mensagem["subject"])
            lista_emails.append({
                "id":i,
                "remetente": remetente,
                "assunto":assunto,
                "corpo":corpo
            })
        return lista_emails

    def verificarObra(nome_da_obra):
        obra = []
        for categoria, sub_obras in obras.items():
            if categoria.lower() in nome_da_obra.lower():
                for obra_email, dados in sub_obras.items():
                    servico = dados[0]
                    departamento = dados[1]
                    obra.append((servico, departamento))
                continue
            for obra_email, dados in sub_obras.items():
                obra_email = obra_email.replace("_", " ")
                if obra_email.lower() in nome_da_obra.lower():
                    servico = dados[0]
                    departamento = dados[1]
                    obra.append((servico, departamento))
        return list(set(obra))
