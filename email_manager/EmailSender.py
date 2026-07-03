import Email
from email.message import EmailMessage
import os
import imaplib
import smtplib
from dotenv import load_dotenv


load_dotenv()

class Email_Sender:
    def __init__(self):
        #self.email_manager = Email()
        self.mail = EmailMessage()
        self.user = os.getenv("EMAIL_USER")
        self.pswd = os.getenv("EMAIL_PSWD")
        self.corpo = ""

    def sent(self, subject, email_reply):
        self.mail['Subject'] = subject
        self.mail['From'] = self.user
        self.mail['To'] = email_reply
        self.mail.set_content(self.corpo, subtype ='html')
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
                servidor.login(self.mail['From'], self.pswd)
                servidor.send_message(self.mail)
                print("Email enviado")
        except Exception as err:
            print(f"Erro ao enviar email: {err}")

    
if __name__ == "__main__":
    mail = Email_Sender()
    #mail.sent(assunto, email_do_remetente)
