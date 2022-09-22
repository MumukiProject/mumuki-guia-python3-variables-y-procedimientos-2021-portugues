  
  def test_o_aumentar_fortuna_duplica_variável_global_reais_na_minha_carteira(self):
    global reais_na_minha_carteira
    reais_na_minha_carteira = 100
    aumentar_fortuna()
    self.assertEqual(reais_na_minha_carteira, 200)


  def test_o_aumentar_fortuna_pode_ser_llamado_muitas_vezes(self):
    global reais_na_minha_carteira
    reais_na_minha_carteira = 30
    aumentar_fortuna()
    aumentar_fortuna()
    aumentar_fortuna()
    self.assertEqual(reais_na_minha_carteira, 240)