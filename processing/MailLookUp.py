class MailLookUp:
    def __init__(self):
        self.obras ={
            "vale": {
                "barragem_obra": ["18", "17"]
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

    def verificarObra(self, nome_da_obra):
        obra = []
        for categoria, sub_obras in self.obras.items():
            if categoria.lower() in nome_da_obra.lower():
                for obra_email, dados in sub_obras.items():
                    servico = dados[0]
                    departamento = dados[1]
                    obra.append((servico, departamento))
                continue
            for obra_email, dados in sub_obras.items():
                obra_email = obra_email.replace("_", " ")
                if obra_email.lower() in nome_da_obra.lower():
                    servico = dados[0]
                    departamento = dados[1]
                    obra.append((servico, departamento))
        return list(set(obra))
