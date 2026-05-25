import unittest

class TestCalculadoraGCS(unittest.TestCase):

    # ====== TESTE MÓDULO A (Básico) ======
    def test_modulo_a_basico(self):
        try:
            import calc_basico
            # Validação lógica exigida no roteiro
            self.assertEqual(calc_basico.somar(2, 3), 5)
            self.assertEqual(calc_basico.subtrair(5, 3), 2)
            self.assertEqual(calc_basico.multiplicar(2, 3), 6)
            self.assertEqual(calc_basico.dividir(6, 2), 3.0)
            
            # Validação de caso de borda (Divisão por zero)
            with self.assertRaises(ValueError):
                calc_basico.dividir(5, 0)
        except ImportError:
            self.skipTest("Módulo calc_basico ainda não disponível no repositório.")

    # ====== TESTE MÓDULO B (Potência) ======
    def test_modulo_b_potencia(self):
        try:
            import calc_potencia
            self.assertEqual(calc_potencia.potencia(2, 3), 8)
            self.assertEqual(calc_potencia.potencia(0, 5), 0)
            self.assertEqual(calc_potencia.potencia(5, 0), 1)
            
            self.assertEqual(calc_potencia.raiz_quadrada(4), 2)
            self.assertEqual(calc_potencia.raiz_quadrada(0), 0)
            # Validação de caso de borda (Raiz de negativo)
            with self.assertRaises(ValueError):
                calc_potencia.raiz_quadrada(-1)
            
            self.assertEqual(calc_potencia.raiz_cubica(27), 3)
            self.assertEqual(calc_potencia.raiz_cubica(0), 0)
        except ImportError:
            self.skipTest("Módulo calc_potencia ainda não disponível no repositório.")

    # ====== TESTE MÓDULO C (Percentual) ======
    def test_modulo_c_percentual(self):
        try:
            import calc_percentual
            self.assertEqual(calc_percentual.percentual(100, 10), 10)
            self.assertEqual(calc_percentual.acrescimo(100, 10), 110)
            self.assertEqual(calc_percentual.desconto(100, 10), 90)
        except ImportError:
            self.skipTest("Módulo calc_percentual ainda não disponível no repositório.")

    # ====== TESTE MÓDULO D (Estatística) ======
    def test_modulo_d_estatistica(self):
        try:
            import calc_estatistica
            # Média
            self.assertEqual(calc_estatistica.media([1, 2, 3, 4, 5]), 3.0)
            self.assertEqual(calc_estatistica.media([10]), 10.0)
            with self.assertRaises(ValueError):
                calc_estatistica.media([])
            
            # Mediana
            self.assertEqual(calc_estatistica.mediana([1, 3, 5]), 3)
            self.assertEqual(calc_estatistica.mediana([1, 2, 3, 4]), 2.5)
            self.assertEqual(calc_estatistica.mediana([5, 1, 3]), 3) # Lista desordenada
            with self.assertRaises(ValueError):
                calc_estatistica.mediana([])
            
            # Desvio Padrão
            self.assertEqual(calc_estatistica.desvio_padrao([1, 2, 3]), 1.0)
            with self.assertRaises(ValueError):
                calc_estatistica.desvio_padrao([1])
            with self.assertRaises(ValueError):
                calc_estatistica.desvio_padrao([])
        except ImportError:
            self.skipTest("Módulo calc_estatistica ainda não disponível no repositório.")

    # ====== TESTE MÓDULO E (Conversão) ======
    def test_modulo_e_conversao(self):
        try:
            import calc_conversao
            self.assertEqual(calc_conversao.celsius_para_fahrenheit(0), 32)
            self.assertEqual(calc_conversao.celsius_para_fahrenheit(100), 212)
            self.assertEqual(calc_conversao.celsius_para_fahrenheit(-40), -40)
            
            # assertAlmostEqual é o método correto do unittest para testar decimais
            self.assertAlmostEqual(calc_conversao.km_para_milhas(1), 0.621371, places=5)
            self.assertEqual(calc_conversao.km_para_milhas(0), 0)
            
            self.assertAlmostEqual(calc_conversao.kg_para_libras(1), 2.20462, places=5)
            self.assertEqual(calc_conversao.kg_para_libras(0), 0)
        except ImportError:
            self.skipTest("Módulo calc_conversao ainda não disponível no repositório.")

if __name__ == "__main__":
    unittest.main()