
  def test_saludar_a_gus_a_las_11_le_dice_buenos_dias(self):
    self.assertEquals(cumprimentar_a("Gus", 11), "Bom dia Gus!")
    
  def test_saludar_a_may_a_las_12_le_dice_buenas_tardes(self):
    self.assertEquals(cumprimentar_a("May", 12), "Boa tarde May!")
    
  def test_saludar_a_lu_a_las_18_le_dice_buenas_tardes(self):
    self.assertEquals(cumprimentar_a("Lu", 18), "Boa tarde Lu!")
    
  def test_saludar_a_guille_a_las_19_le_dice_buenas_noches(self):
    self.assertEquals(cumprimentar_a("Guille", 19), "Boa noite Guille!")
  
  def test_saludar_a_jor_a_las_20_le_dice_buenas_noches(self):
    self.assertEquals(cumprimentar_a("Jor", 20), "Boa noite Jor!")  