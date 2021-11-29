from datetime import datetime, timedelta

class DatasBr:
    #retorna o dia do cadastro
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

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

    # retorna a data formatada
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    # retorna o tempo de cadastro
    def tempo_cadastro(self):
        return datetime.today() - self.momento_cadastro

    # mais formatos neste link com a documentação
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior


