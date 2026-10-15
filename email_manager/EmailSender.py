from email.message import EmailMessage
import os
import smtplib
from dotenv import load_dotenv


load_dotenv()

class EmailSender:
    def __init__(self): 
        self.user = os.getenv("EMAIL_USER")
        self.pswd = os.getenv("EMAIL_PSWD")
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", 465))

    def _validate_subject(self, subject:str)->str:
        if not subject:
            raise ValueError("O assunto não pode ser vazio.")
        return subject.strip()

    def _validate_text(self, text:str)->str:
        pass # sem regra para validar o texto do email

    def send(self, subject:str, recipient:str, body:str):
        subject = self._validate_subject(subject)
        body = self._validate_text(text)

        msg = EmailMessage()
        
        msg['Subject'] = subject
        msg['From'] = self.user
        msg['To'] = recipient
        # Estou usando um email pre-setado para teste
        # O correto é puxar o email do remetente
        msg.set_content(body, subtype ='html')
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(self.user, self.pswd)
                server.send_message(msg)
                print("Email enviado")
        except Exception as err:
            print(f"Erro ao enviar email: {err}"

if __name__ == "__main__":
    sender = EmailSender()
    sender.send("a","@mail","c")#só pra testar

