from email_reader import Email
from processamento import MailLookUp

gerenciador_Emails = Email()
validar_Obras = MailLookUp()

gerenciador_Emails.conectar()

lista_emails = gerenciador_Emails.catch_emails()

for email in lista_emails:
    print(f"Id: {email['id']}")
    print(f"remetente: {email['remetente']}")
    print(f"assunto: {email['assunto']}")
    print(f"corpo: {email['corpo']}")
    print(f"{'-'*30}{'\n'*2}")


