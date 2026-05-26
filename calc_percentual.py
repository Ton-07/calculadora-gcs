# calc_percentual.py
# Módulo C — Percentual
# Autor: Pedro Lucas de Souza Cremonini
# Branch: feature/percentual

def percentual(valor, porcentagem):
    return (valor * porcentagem) / 100


def acrescimo(valor, porcentagem):
    return valor + percentual(valor, porcentagem)


def desconto(valor, porcentagem):
    return valor - percentual(valor, porcentagem)
