from .ServiceLookUp import ServiceLookUp
from email_manager import Email


class EmailLookUp:
    def __init__(self, emails):
        self.key_word = "efetivo"
        self.service_list = dict()
        self.qualify_service = ServiceLookUp()
        self.email_list = self._validation_list(emails)

    def _validation_list(self, emails) -> list[dict]:
        if not emails:
            print("Nenhum email na caixa de entrada!")
            return []
        if not isinstance(emails, list):
            raise TypeError(f"Espereva uma lista de email, recebeu: {type(emails).__name__}")
        return emails
    
    def mail_resolver(self):
        service_mail = self.email_list
        for email in service_mail:
            if self.key_word in email["assunto"].strip().lower():
                service_code = self.qualify_service.service_resolver(email['corpo']).copy()
                if service_code:
                    self.service_list.update({email['id']:service_code})
        return self.service_list

if __name__ == "__main__":
    
    emails = Email()
    emails.conectar()
    email = EmailLookUp(emails)
    emails.desconectar()
    print(email.email_list)
    

    
