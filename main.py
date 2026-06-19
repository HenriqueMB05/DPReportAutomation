from email_reader import Email
from parsing import EmailLookUp, ServiceLookUp

email_manager = Email()
service_manager = ServiceLookUp()

qualify_email = EmailLookUp(email_manager, service_manager)
service_list = qualify_email.mail_resolver()

for email_id, work_field in service_list.items(): 
    print(f"{'-'*30}")
    print(email_id)
    for k, v in enumerate(work_field):
        print(v)


