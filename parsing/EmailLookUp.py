from .ServiceLookUp import ServiceLookUp
from email_reader.Email import Email

class EmailLookUp:
    def __init__(self):
        self.email_manager = Email()
        self.key_word = "efetivo"
        self.service_list = {}
        self.qualify_service = ServiceLookUp()
        self.email_list = self._validation_list()

    def _validation_list(self):
        try:
            self.email_manager.conectar()
            emails = self.email_manager.catch_emails()
            if not emails:
                print("Nenhum email na caixa de entrada!")
                return[]
            return emails
        except Exception as err:
            print(f"Erro ao abrir/buscar emails: {err}")
            return []
    
    def mail_resolver(self):
        service_mail = self.email_list
        for email in service_mail:
            if self.key_word in email["assunto"].strip().lower():
                service_code = self.qualify_service.service_resolver(email['corpo']).copy()
                if service_code:
                    self.service_list.update({email['id']:service_code})
        return self.service_list
