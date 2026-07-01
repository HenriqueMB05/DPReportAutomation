import Email
from email.message import EmailMessage
import os
import imaplib
import smtplib
from dotenv import load_dotenv


load_dotenv()

class EmailSender:
    def __init__(self): 
        self.email = EmailMessage()
        self.corpo = r"<p>Olá sior cookie pisca, nois que rraquia ceu emiu, pu favor nois da a senha."
        self.user = os.getenv("EMAIL_USER")
        self.pswd = os.getenv("EMAIL_PSWD")

    def sent(self):
        self.email['Subject'] = "Pru favo"
        self.email['From'] = self.user
        self.email['To'] = os.getenv("EMAIL_FROM")
        self.email.set_content(self.corpo, subtype ='html')
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
                servidor.login(self.email['From'], self.pswd)
                servidor.send_message(self.email)
        except Exception as err:
            print(f"Erro ao enviar email: {err}")

    
if __name__ == "__main__":
    mail = EmailSender()
    mail.sent()
