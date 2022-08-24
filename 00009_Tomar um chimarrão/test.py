  
  def test_cebar_mate_disminuye_en_30_ml_el_agua_del_termo(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 1000
    fazer_chimarreo()
    self.assertEqual(agua_da_garrafa_termica, 970)


  def test_cebar_3_mates_disminuye_en_90_ml_el_agua_del_termo(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 1000
    fazer_chimarreo()
    fazer_chimarreo()
    fazer_chimarreo()
    self.assertEqual(agua_da_garrafa_termica, 910)