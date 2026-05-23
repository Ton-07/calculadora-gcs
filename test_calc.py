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
    print("Deu bom os testes")