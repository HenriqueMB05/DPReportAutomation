from email_reader import Email
from parsing import ServiceLookUp

email_manager = Email()
qualify_service = ServiceLookUp()

email_manager.conectar()

email_list = email_manager.catch_emails()

service_list = {}
for email in email_list:
    subject_text = email["assunto"].lower().split("\n")
    for mail in subject_text:
        print(mail)
        if "efetivo".lower() in mail:
            service_code = qualify_service.service_resolver(email['corpo']).copy()
            if service_code:
                service_list.update({email['id']: service_code})

for email_id, work_field in service_list.items(): 
    print(f"{'-'*30}")
    print(email_id)
    for k, v in enumerate(work_field):
        print(v)


