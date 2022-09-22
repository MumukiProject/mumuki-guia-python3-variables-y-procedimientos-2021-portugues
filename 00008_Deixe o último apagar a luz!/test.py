  
  def test_se_a_mochila_estava_aberta_ao_executar_usar_zíper_passa_a_estar_fechada(self):
    usar_ziper()
    self.assertFalse(mochila_abierta)
  
  
  def test_se_a_mochila_estava_fechada_ao_executar_usar_zíper_passa_a_estar_aberta(self):
    global mochila_abierta
    mochila_abierta = False
    usar_ziper()
    self.assertTrue(mochila_abierta)
  
  
  def test_se_a_mochila_estava_aberta_ao_executar_usar_zíper_duas_vezes_continua_estando_aberta(self):
    usar_ziper()
    usar_ziper()
    self.assertTrue(mochila_abierta)