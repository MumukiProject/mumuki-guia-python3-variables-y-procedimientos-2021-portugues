  
  def test_encher_garrafa_térmica_com_200_como_argumento_aumenta_para_200_a_água_da_garrafa_térmica(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 600
    colocar_agua_na_garrafa(200)
    self.assertEqual(agua_da_garrafa_termica, 800)


  def test_encher_garrafa_térmica_com_500_como_argumento_aumenta_para_500_a_água_da_garrafa_térmica(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 200
    colocar_agua_na_garrafa(500)
    self.assertEqual(agua_da_garrafa_termica, 700)