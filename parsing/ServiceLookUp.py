class ServiceLookUp:
    def __init__(self): 
        self.services ={
            "vale": {
                "usina_da_paz":["1","43"],
                "barragem_cnpj": ["1", "18"], 
                "operação": ["40", "39"], 
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
                "candeias":["42", "41"],
                "ji-parana":["28","27"],
                "tapa_buraco":["31","30"],
                "rio_da_vala":["33","32"],
                "br-230": ["41","40"],
                "br-158": ["43", "42"]
            }
        }
    
    @property
    def flat_services(self):
        return{
            obra: servicos
            for obras in self.services.values()
            for obra , servicos in obras.items()
        }


    def service_resolver(self, name_service):
        services = name_service.lower().strip()

        if "todos" in services or "todas" in services:
            return list(self.flat_services.values())
        
        if services in self.services:
            return[tuple(dados) for dados in self.services[services].values()]

        if services in self.flat_services:
            return[self.flat_services[services]]
        
        return []

lista = ['usina_da_paz', 'barragem_cnpj', 'todos']

if __name__ == '__main__':
    servico = ServiceLookUp()
    print(*(x for x in lista))
    print([servico.service_resolver(set(x)) for x in lista])
