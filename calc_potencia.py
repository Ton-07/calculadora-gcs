# calc_potencia.py
# Módulo B — Operações de Potência
# Autor: Gabriel Mattos de Aquino
# Branch: feature/modulo-potencia

import math

def potencia(base, expoente):
    """Retorna a base elevada ao expoente."""
    return base ** expoente

def raiz_quadrada(a):
    """Retorna a raiz quadrada de a."""
    if a < 0:
        raise ValueError("Raiz quadrada de número negativo invalida")
    return a ** 0.5

def raiz_cubica(a):
    """Retorna a raiz cúbica de a."""
    return a ** (1/3)

