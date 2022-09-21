
  def test_cumprimentar_a_gus_às_11_diz_bom_dia(self):
    self.assertEquals(cumprimentar_a("Gus", 11), "Bom dia Gus!")
    
  def test_cumprimentar_a_may_às_12_diz_boa_tarde(self):
    self.assertEquals(cumprimentar_a("May", 12), "Boa tarde May!")
    
  def test_cumprimentar_a_lu_às_18_diz_boa_tarde(self):
    self.assertEquals(cumprimentar_a("Lu", 18), "Boa tarde Lu!")
    
  def test_cumprimentar_a_guille_às_19_diz_boa_noite(self):
    self.assertEquals(cumprimentar_a("Guille", 19), "Boa noite Guille!")
  
  def test_cumprimentar_a_jor_às_20_diz_boa_noite(self):
    self.assertEquals(cumprimentar_a("Jor", 20), "Boa noite Jor!")  