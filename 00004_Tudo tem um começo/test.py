  
  def test_o_elevador_não_está_sobrecarregado_com_4_pessoas_se_o_peso_médio_pessoa_em_quilogramas_é_70(self):
    global peso_medio_pessoa_em_quilogramas
    peso_medio_pessoa_em_quilogramas = 70
    self.assertFalse(elevador_sobrecarregado(4))

  def test_o_elevador_está_sobrecarregado_com_4_pessoas_se_o_peso_médio_pessoa_em_quilogramas_é_80(self):
    global peso_medio_pessoa_em_quilogramas
    peso_medio_pessoa_em_quilogramas = 80
    self.assertTrue(elevador_sobrecarregado(4))

  def test_o_elevador_não_está_sobrecarregado_com_2_pessoas_se_o_peso_médio_pessoa_em_quilogramas_é_80(self):
    global peso_medio_pessoa_em_quilogramas
    peso_medio_pessoa_em_quilogramas = 80
    self.assertFalse(elevador_sobrecarregado(2))

  def test_o_elevador_está_sobrecarregado_com_5_pessoas_se_o_peso_médio_pessoa_em_quilogramas_é_80(self):
    global peso_medio_pessoa_em_quilogramas
    peso_medio_pessoa_em_quilogramas = 80
    self.assertTrue(elevador_sobrecarregado(5))