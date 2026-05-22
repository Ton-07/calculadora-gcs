# calc_basico.py
# Módulo A — Operações Básicas
# Autor: Jonathan Pereira do Amaral
# Branch: feature/modulo-basico

def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtrair(a, b):
    """Retorna a diferença de a e b."""
    return a - b

def multiplicar(a, b):
    """Retorna o produto de a e b."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de a por b.
    Lança ValueError se b == 0."""
    if b == 0:
        raise ValueError("Divisão por zero invalida")
    return a / b

