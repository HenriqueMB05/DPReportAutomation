from email_reader import Email
from processing import ServiceLookUp

email_manager = Email()
qualify_service = ServiceLookUp()

email_manager.conectar()

email_list = email_manager.catch_emails()

obras = []

for email in email_list:
    subject_text = email["assunto"].lower().split("\n")
    for mail in subject_text:
        print(mail)
        if "efetivo".lower() in mail:
            print(f"id: {email['id']}")
            print(f"Assunto: {email['assunto']}")
            print(f"Corpo: {email['corpo']}")
            obras = qualify_service.service_resolver(email['corpo']).copy()

for i, k in enumerate(obras):
    print(f"{i} - {k}")



