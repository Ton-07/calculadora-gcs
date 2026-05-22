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