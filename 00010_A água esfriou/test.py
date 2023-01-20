
  def test_esvaziar_a_garrafa_térmica_deixa_em_0_a_água_da_garrafa_térmica_se_tivesse_1000(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 1000
    esvaziar_garrafa()
    self.assertEqual(agua_da_garrafa_termica, 0)

  
  def test_esvaziar_a_garrafa_térmica_deixa_em_0_a_água_da_garrafa_térmica_se_tivesse_500(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 500
    esvaziar_garrafa()
    self.assertEqual(agua_da_garrafa_termica, 0)

  
  def test_esvaziar_a_garrafa_térmica_deixa_em_0_a_água_da_garrafa_térmica_se_tivesse_200(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 200
    esvaziar_garrafa()
    self.assertEqual(agua_da_garrafa_termica, 0)



  def test_encher_garrafa_térmica_deixa_em_1000_a_água_da_garrafa_térmica(self):
    global agua_da_garrafa_termica
    agua_da_garrafa_termica = 80
    encher_garrafa()
    self.assertEqual(agua_da_garrafa_termica, 1000)