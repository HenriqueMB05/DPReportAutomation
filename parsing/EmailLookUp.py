from .ServiceLookUp import ServiceLookUp

class EmailLookUp:
    def __init__(self, emails):
        self.email_manager = emails
        self.key_word = "efetivo"
        self.service_list = dict()
        self.qualify_service = ServiceLookUp()
        self.email_list = self._validation_list()

    def _validation_list(self):
        try:
            if not self.email_manager:
                print("Nenhum email na caixa de entrada!")
                return
            return self.email_manager
        except Exception as err:
            raise f"Erro ao abrir/buscar emails: {err}"
    
    def mail_resolver(self):
        service_mail = self.email_list
        for email in service_mail:
            if self.key_word in email["assunto"].strip().lower():
                service_code = self.qualify_service.service_resolver(email['corpo']).copy()
                if service_code:
                    self.service_list.update({email['id']:service_code})
        return self.service_list
