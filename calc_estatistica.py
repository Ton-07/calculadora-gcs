# Módulo D - Estatística
# Autor: Angelo Antonio 
# Branch: feature/modulo-estatistica

import math

def media(valores):
    """Retorna a média aritmética de uma lista de valores."""
    if not valores:
        raise ValueError("A lista de valores não pode estar vazia.")
    return sum(valores) / len(valores)

def mediana(valores):
    """Retorna a mediana de uma lista de valores."""
    if not valores:
        raise ValueError("A lista de valores não pode estar vazia.")
    
    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)
    meio = n // 2
    
    if n % 2 == 0:
        return (valores_ordenados[meio - 1] + valores_ordenados[meio]) / 2.0
    else:
        return valores_ordenados[meio]

def desvio_padrao(valores):
    """Retorna o desvio padrão amostral de uma lista de valores."""
    if not valores or len(valores) < 2:
        raise ValueError("É necessário pelo menos dois valores para calcular o desvio padrão amostral.")
    
    m = media(valores)
    soma_quadrados = sum((x - m) ** 2 for x in valores)
    variancia = soma_quadrados / (len(valores) - 1)
    
    return math.sqrt(variancia)