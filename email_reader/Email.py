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
        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PSWD")
        self.mail = None

    def conectar(self):
        self.mail = imaplib.IMAP4_SSL("imap.gmail.com")
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

        for index in ids:
            status, dados = self.mail.fetch(index, "(BODY.PEEK[])")
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

            corpo_limpo = EmailReplyParser.parse_reply(corpo)
            remetente = self._decode_cabecalho(mensagem["from"])
            assunto = self._decode_cabecalho(mensagem["subject"])
            lista_emails.append({
                "id":index,
                "remetente": remetente,
                "assunto":assunto,
                "corpo":corpo_limpo
            })
        return lista_emails

