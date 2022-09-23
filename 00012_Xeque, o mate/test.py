  
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
    
  def test_fazer_chimarrão_aumenta_para_30_ml_a_água_do_mate(self):
    global agua_do_chimarrao
    agua_do_chimarrao = 0
    fazer_chimarrao()
    self.assertEqual(agua_do_chimarrao, 30)
    
  def test_tomar_chimarrão_deixa_em_0_ml_a_água_do_chimarrão(self):
    global agua_do_chimarrao
    agua_do_chimarrao = 20
    tomar_chimarrao()
    self.assertEqual(agua_do_chimarrao, 0)