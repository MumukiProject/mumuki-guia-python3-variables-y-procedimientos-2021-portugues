  
  def test_o_perímetro_de_um_círculo_de_raio_1_é_correto(self):
    self.assertEqual(perimetro_circulo(1), 6.28318530717958)
  
  def test_o_perímetro_de_um_círculo_de_raio_2_é_correto(self):
    self.assertEqual(perimetro_circulo(2), 12.56637061435916)
  
  def test_o_perímetro_de_um_círculo_de_raio_0_é_correto(self):
    self.assertEqual(perimetro_circulo(0), 0)
  
  def test_a_área_de_um_círculo_de_raio_1_é_correto(self):
    self.assertEqual(area_circulo(1), 3.14159265358979)
  
  def test_a_área_de_um_círculo_de_raio_2_é_correto(self):
    self.assertEqual(area_circulo(2), 12.56637061435916)
  
  def test_a_área_de_um_círculo_de_raio_0_é_correto(self):
    self.assertEqual(area_circulo(0), 0)

