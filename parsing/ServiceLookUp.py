class ServiceLookUp:
    def __init__(self): 
        self.services ={
            "vale": {
                "barragem_obra": ["18", "17"],
                "barragem_cnpj": ["1", "18"], 
                "operação": ["38", "37"], 
                "infra":["23", "22"], 
                "remanescente": ["25", "24"]
            },
            "publica": {
                "cnpj":["1", "1,3"],
                "oficina":["1","23"],
                "goinia":["1","35"],
                "trilha_mirante":["20","19"],
                "capanema": ["21","20"],
                "sebrae": ["29","28"],
                "parque_do_mirante":["34", "33"],
                "parque_linear":["37","36"]
            },
            "consorcio":{
                "candeias":["27", "26"],
                "ji-parana":["28","27"],
                "tapa_buraco":["31","30"],
                "rio_da_vala":["33","32"],
                "rio_caete":["35","34"]
            }
        }
        
    def service_resolver(self, name_service):
        service = []
        for category, sub_services in self.services.items():
            if "todos" in name_service.lower() or "todas" in name_service.lower():
                for email_service, data in sub_services.items():
                    field_work = data[0]
                    department = data[1]
                    service.append((field_work, department))
            if category.lower() in name_service.lower():
                for email_service, data in sub_services.items():
                    field_work = data[0]
                    department = data[1]
                    service.append((field_work, department))
                continue
            for email_service, data in sub_services.items():
                email_service = email_service.replace("_", " ")
                if email_service.lower() in name_service.lower():
                    field_work = data[0]
                    department = data[1]
                    service.append((field_work, department))
        return list(set(service))


lista = ['barragem obra', 'barragem cnpj']

if __name__ == '__main__':
    service_resolver()
