import calc_basico

# ====== TESTE MODULO A ======

def testar_operacoes():
    """validacao logica de soma e subtracao"""
    assert calc_basico.somar(2, 3) == 5
    assert calc_basico.subtrair(5, 3) == 2

    """validacao logica de multiplicacao e divisao"""
    assert calc_basico.multiplicar(2, 3) == 6
    assert calc_basico.dividir(6, 2) == 3.0

    """validacao critica de caso de borda exigida no checklist"""
    falha_detectada = False
    try:
        calc_basico.dividir(5, 0)
    except ValueError:
        falha_detectada = True
    
    if falha_detectada == False:
        raise AssertionError("erro critico: divisao por zero nao bloqueada")
    
    print("testes do modulo a executados com exatidao")

if __name__ == "__main__":
    testar_operacoes()

# ====== TESTE MODULO B ======
import calc_potencia

def testar_modulo():
    #Teste de potencia
    assert calc_potencia.potencia(2, 3) == 8
    assert calc_potencia.potencia(0, 5) == 0
    assert calc_potencia.potencia(5, 0) == 1
    #Teste de raiz quadrada
    assert calc_potencia.raiz_quadrada(4) == 2
    assert calc_potencia.raiz_quadrada(0) == 0
    
    #Teste de raiz cubica
    assert calc_potencia.raiz_cubica(27) == 3
    assert calc_potencia.raiz_cubica(0) == 0

    print("testes do modulo b executados com exatidao")

# ====== TESTE MODULO D ======
from calc_estatistica import media, mediana, desvio_padrao

def rodar_testes():
    print("Iniciando testes do Módulo de Estatística...\n")

    #Testes da Média 
    print("1. Testando media()...")
    assert media([1, 2, 3, 4, 5]) == 3.0, "Erro na média"
    assert media([10]) == 10.0, "Erro na média com 1 elemento"
    
    try:
        media([])
        print("ERRO: media([]) não lançou a exceção ValueError!")
    except ValueError:
        print("Caso de borda tratado: media([]) bloqueada com sucesso.")


    # --- Testes da Mediana ---
    print("\n2. Testando mediana()...")
    assert mediana([1, 3, 5]) == 3, "Erro na mediana ímpar"
    assert mediana([1, 2, 3, 4]) == 2.5, "Erro na mediana par"
    assert mediana([5, 1, 3]) == 3, "Erro na mediana desordenada"
    
    try:
        mediana([])
        print("ERRO: mediana([]) não lançou a exceção ValueError!")
    except ValueError:
        print("Caso de borda tratado: mediana([]) bloqueada com sucesso.")


    # --- Testes do Desvio Padrão ---
    print("\n3. Testando desvio_padrao()...")
    assert desvio_padrao([1, 2, 3]) == 1.0, "Erro no desvio padrão"
    
    try:
        desvio_padrao([1])
        print("ERRO: desvio_padrao() com 1 elemento não lançou exceção!")
    except ValueError:
        print("Caso de borda tratado: desvio_padrao([1]) bloqueado com sucesso.")


    print("\nTodos os testes passaram com sucesso!")

# Executa a função de testes
if __name__ == '__main__':
    rodar_testes()


# ====== TESTE MODULO E ======

from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras

def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(100) == 212
    assert celsius_para_fahrenheit(-40) == -40

def test_km_para_milhas():
    assert round(km_para_milhas(1), 6) == 0.621371
    assert round(km_para_milhas(0), 6) == 0

def test_kg_para_libras():
    assert round(kg_para_libras(1), 5) == 2.20462
    assert round(kg_para_libras(0), 5) == 0

if __name__ == "__main__":
    test_celsius_para_fahrenheit()
    test_km_para_milhas()
    test_kg_para_libras()
    print("Deu bom os testes!")