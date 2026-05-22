def menu():
    print("=== Calculadora GCS ===\n")
    try:
        from calc_basico import somar, subtrair, multiplicar, dividir
        print("Módulo Básico carregado.")
        print("  2 + 3 =", somar(2, 3))
    except ImportError:
        print("Módulo Básico ainda não disponível.")

    try:
        from calc_potencia import potencia, raiz_quadrada
        print("Módulo Potência carregado.")
        print("  2^10 =", potencia(2, 10))
    except ImportError:
        print("Módulo Potência ainda não disponível.")


    # ... adicionar try/except para cada módulo restante ...


if __name__ == "__main__":
    menu()

