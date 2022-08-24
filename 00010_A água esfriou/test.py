  
  def test_vaciar_termo_deja_en_0_el_agua_del_termo(self):
    global agua_da_garrafa
    agua_da_garrafa = 1000
    esvaziar_garrafa()
    self.assertEqual(agua_da_garrafa, 0)


  def test_llenar_termo_deja_en_1000_el_agua_del_termo(self):
    global agua_da_garrafa
    agua_da_garrafa = 80
    encher_garrafa()
    self.assertEqual(agua_da_garrafa, 1000)