from email_manager import Email
from parsing import ServiceLookUp, EmailLookUp
qualify_email = EmailLookUp()

service_list = qualify_email.mail_resolver()
for email_id, work_field in service_list.items():
    print(f"{'-'*30}")
    print(email_id)
    for k, v in enumerate(work_field):
        print(v)


#if __name__ == "__main__":
#   services_teste = ServiceLookUp()
#  obras = services_teste.flat_services
# print(obras)
