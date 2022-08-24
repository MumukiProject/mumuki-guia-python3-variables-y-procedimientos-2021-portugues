agua_do_chimarrao = 0
agua_da_garrafa_termica = 1000

def fazer_chimarrao():
  global agua_do_chimarrao
  global agua_da_garrafa_termica
  agua_da_garrafa_termica -= 30
  agua_do_chimarrao += 30
  
def tomar_chimarrao():
  global agua_do_chimarrao
  agua_do_chimarrao = 0
  
def passar():
  pass