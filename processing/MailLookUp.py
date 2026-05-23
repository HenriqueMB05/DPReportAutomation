class MailLookUp:
    def __init__(self):
        self.obras ={
            "vale": {
                "barragem obra": ["18", None],
                "barragem_cnpj": ["1", "18"], 
                "operacao": ["38", None], 
                "infra":["23", None], 
                "remanescente": ["25", None]
            },
            "publica": {
                "cnpj":["1", "1,3"],
                "oficina":["1","23"],
                "goinia":["1","35"],
                "trilha_mirante":["20",None],
                "capanema": ["21",None],
                "sebrae": ["29", None],
                "pq_mirante":["34", None],
                "pq_linear":["37",None]
            },
            "consorcio":{
                "candeias":["27", None],
                "ji-parana":["28",None],
                "tapa_buraco":["31",None],
                "rio_da_vala":["33",None],
                "rio_caete":["35",None]
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
