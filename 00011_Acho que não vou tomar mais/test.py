  
  def test_cargar_termo_con_200_como_argumento_aumenta_en_200_el_agua_del_termo(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 600
    colocar_agua_na_garrafa(200)
    self.assertEqual(agua_da_garrafa_termica, 800)


  def test_cargar_termo_con_500_como_argumento_aumenta_en_500_el_agua_del_termo(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 200
    colocar_agua_na_garrafa(500)
    self.assertEqual(agua_da_garrafa_termica, 700)