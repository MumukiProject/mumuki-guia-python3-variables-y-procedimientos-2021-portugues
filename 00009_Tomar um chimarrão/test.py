  
  def test_fazer_chimarrão_diminui_para_30_ml_a_água_da_garrafa_térmica(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 1000
    fazer_chimarrao()
    self.assertEqual(agua_da_garrafa_termica, 970)


  def test_fazer_3_chimarrões_diminui_para_90_ml_a_água_da_garrafa_térmica(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 1000
    fazer_chimarrao()
    fazer_chimarrao()
    fazer_chimarrao()
    self.assertEqual(agua_da_garrafa_termica, 910)