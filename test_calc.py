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
import unittest
from calc_estatistica import media, mediana, desvio_padrao

class TestCalcEstatistica(unittest.TestCase):

    def test_media(self):
        # Casos normais
        self.assertEqual(media([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(media([10]), 10.0)
        
        # Caso de borda: lista vazia deve lançar ValueError
        with self.assertRaises(ValueError):
            media([])

    def test_mediana(self):
        # Casos normais (ímpar e par de elementos)
        self.assertEqual(mediana([1, 3, 5]), 3)
        self.assertEqual(mediana([1, 2, 3, 4]), 2.5)
        self.assertEqual(mediana([5, 1, 3]), 3) # Lista desordenada
        
        # Caso de borda: lista vazia deve lançar ValueError
        with self.assertRaises(ValueError):
            mediana([])

    def test_desvio_padrao(self):
        # Caso normal
        self.assertEqual(desvio_padrao([1, 2, 3]), 1.0)
        
        # Casos de borda: listas com menos de 2 elementos devem lançar ValueError
        with self.assertRaises(ValueError):
            desvio_padrao([1])
        with self.assertRaises(ValueError):
            desvio_padrao([])

if __name__ == '__main__':
    unittest.main()


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