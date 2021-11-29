from datetime import datetime, timedelta

class DatasBr:
    #retorna o dia do cadastro
    def __init__(self):
        self.momento_cadastro = datetime.today()

    #retorna o mes do cadastro
    def mes_cadastro(self):
        mes_cadastro = self.momento_cadastro.month -1
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abriu", "maio", "junho", "julho",
            "agosto", "setembro", "outubro",
            "novembro", "dezembro"
        ]
        return meses_do_ano[mes_cadastro]

    # retorna dia da semana
    def dia_semana(self):
        dia_semana = self.momento_cadastro.weekday()
        dia_semana_lista = [
            "segunda", "terça", "quarta",
            "quinta", "sexta", "sabado", "domingo"
        ]
        return dia_semana_lista[dia_semana]
