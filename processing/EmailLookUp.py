class EmailLookUp:
    def __init__(self):
        self.key_word = "efetivo"
        self.list_email = validation_list(email)

    
    def _validation_list(self, email: list):
        if not email:
            print("Não há email na caixa de entrada")
            return
        return email
            

    def mail_resolver(self):
        mails = []
        for k, v in self.list_email.items():
            if self.key_word in k:
                continue
