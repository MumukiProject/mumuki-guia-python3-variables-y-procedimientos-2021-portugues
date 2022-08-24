  
  def test_el_ascensor_no_esta_sobrecargado_con_4_personas_si_el_peso_promedio_persona_en_kilogramos_es_70(self):
    global peso_medio_pessoa_em_quilogramas
    peso_medio_pessoa_em_quilogramas = 70
    self.assertFalse(elevador_sobrecarregado(4))

  def test_el_ascensor_esta_sobrecargado_con_4_personas_si_el_peso_promedio_persona_en_kilogramos_es_80(self):
    global peso_medio_pessoa_em_quilogramas
    peso_medio_pessoa_em_quilogramas = 80
    self.assertTrue(elevador_sobrecarregado(4))

  def test_el_ascensor_no_esta_sobrecargado_con_2_personas_si_el_peso_promedio_persona_en_kilogramos_es_80(self):
    global peso_medio_pessoa_em_quilogramas
    peso_medio_pessoa_em_quilogramas = 80
    self.assertFalse(elevador_sobrecarregado(2))

  def test_el_ascensor_esta_sobrecargado_con_5_personas_si_el_peso_promedio_persona_en_kilogramos_es_80(self):
    global peso_medio_pessoa_em_quilogramas
    peso_medio_pessoa_em_quilogramas = 80
    self.assertTrue(elevador_sobrecarregado(5))