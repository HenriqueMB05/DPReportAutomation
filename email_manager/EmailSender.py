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
        self.corpo = self._validate_text(corpo)
        self.subject = self._validate_subject(subject)
        self.user = os.getenv("EMAIL_USER")
        self.pswd = os.getenv("EMAIL_PSWD")

    def sent(self):
        self.email['Subject'] = 
        self.email['From'] = self.user
        self.email['To'] = os.getenv("EMAIL_FROM") 
        # Estou usando um email pre-setado para teste
        # O correto é puxar o email do remetente
        self.email.set_content(self.corpo, subtype ='html')
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
                servidor.login(self.email['From'], self.pswd)
                servidor.send_message(self.email)
        except Exception as err:
            print(f"Erro ao enviar email: {err}")
    
    def _validate_subject(self, subject):

    
if __name__ == "__main__":
    mail = EmailSender()
    mail.sent()
