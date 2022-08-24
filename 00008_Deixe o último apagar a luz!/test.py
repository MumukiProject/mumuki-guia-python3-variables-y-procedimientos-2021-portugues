  
  def test_si_la_mochila_estaba_abierta_al_ejecutar_usar_cierre_pasa_a_estar_cerrada(self):
    usar_ziper()
    self.assertFalse(mochila_abierta)
  
  
  def test_si_la_mochila_estaba_cerrada_al_ejecutar_usar_cierre_pasa_a_estar_abierta(self):
    global mochila_abierta
    mochila_abierta = False
    usar_ziper()
    self.assertTrue(mochila_abierta)
  
  
  def test_si_la_mochila_estaba_abierta_al_ejecutar_usar_cierre_dos_veces_sigue_estando_abierta(self):
    usar_ziper()
    usar_ziper()
    self.assertTrue(mochila_abierta)