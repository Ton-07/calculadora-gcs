def menu():
    print("=== Calculadora GCS ===\n")
    
    # Módulo A - Básico
    try:
        from calc_basico import somar, subtrair, multiplicar, dividir
        print("Módulo Básico carregado.")
        print("  2 + 3 =", somar(2, 3))
        print("  10 / 2 =", dividir(10, 2))
    except ImportError:
        print("Módulo Básico ainda não disponível.")

    # Módulo B - Potência
    try:
        from calc_potencia import potencia, raiz_quadrada, raiz_cubica
        print("Módulo Potência carregado.")
        print("  2^10 =", potencia(2, 10))
        print("  Raiz quadrada de 16 =", raiz_quadrada(16))
    except ImportError:
        print("Módulo Potência ainda não disponível.")

    # Módulo C - Percentual (Será carregado quando o responsável fizer o merge)
    try:
        from calc_percentual import percentual, acrescimo, desconto
        print("Módulo Percentual carregado.")
        print("  10% de 100 =", percentual(100, 10))
    except ImportError:
        print("Módulo Percentual ainda não disponível.")

    # Módulo D - Estatística
    try:
        from calc_estatistica import media, mediana, desvio_padrao
        print("Módulo Estatística carregado.")
        print("  Média de [1, 2, 3, 4, 5] =", media([1, 2, 3, 4, 5]))
    except ImportError:
        print("Módulo Estatística ainda não disponível.")

    # Módulo E - Conversão
    try:
        from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras
        print("Módulo Conversão carregado.")
        print("  0°C em Fahrenheit =", celsius_para_fahrenheit(0))
    except ImportError:
        print("Módulo Conversão ainda não disponível.")


if __name__ == "__main__":
    menu()