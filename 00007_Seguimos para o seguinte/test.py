  
  def test_el_aumentar_fortuna_duplica_variable_global_pesos_en_mi_billetera(self):
    global reais_na_minha_carteira
    reais_na_minha_carteira = 100
    aumentar_fortuna()
    self.assertEqual(reais_na_minha_carteira, 200)


  def test_el_aumentar_fortuna_se_puede_llamar_muchas_veces(self):
    global reais_na_minha_carteira
    reais_na_minha_carteira = 30
    aumentar_fortuna()
    aumentar_fortuna()
    aumentar_fortuna()
    self.assertEqual(reais_na_minha_carteira, 240)