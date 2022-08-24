  
  def test_cebar_mate_disminuye_en_30_ml_el_agua_del_termo(self):
    global agua_do_chimarrao
    agua_do_chimarrao = 1000
    fazer_chimarrao()
    self.assertEqual(agua_do_chimarrao, 970)

  def test_cebar_3_mates_disminuye_en_90_ml_el_agua_del_termo(self):
    global agua_do_chimarrao
    agua_do_chimarrao = 1000
    fazer_chimarrao()
    fazer_chimarrao()
    fazer_chimarrao()
    self.assertEqual(agua_do_chimarrao, 910)
    
  def test_cebar_mate_aumenta_en_30_ml_el_agua_del_mate(self):
    global agua_do_chimarrao
    agua_do_chimarrao = 0
    fazer_chimarrao()
    self.assertEqual(agua_do_chimarrao, 30)
    
  def test_tomar_mate_deja_en_0_ml_el_agua_del_mate(self):
    global agua_do_chimarrao
    agua_do_chimarrao = 20
    tomar_chimarrao()
    self.assertEqual(agua_do_chimarrao, 0)