from datetime import datetime

calcular_agora = datetime.now  # nao retirar pq é usado para os testes


def minutos_de_vida(nascimento):
    agora = calcular_agora()
    delta = agora - nascimento
    return int(delta.total_seconds()) // 60
