class futbolista():

  equipo = None
  habilidad = None
  edad = None
  genero = None
  liga = None
  posicion = None
  numero = None
  estadisticas = None
  patrocinadores = None
  nacionalidad = None

  def __init__(self):
    print("Clase futbolista")

  def correr (self):
    print ("Metodo correr")

  def patear (self):
    print("Metodo patear")

  def proteger (self):
    print("Metodo proteger")

  def jugar (self):
    print("Metodo jugar")

  def vender (self):
    print ("Metodo vender")

ronaldo = futbolista()
ronaldo.equipo="Juventus F. C"
ronaldo.habilidad="si"
ronaldo.edad="35 años"
ronaldo.genero="Masculino"
ronaldo.nacionalidad="Portugués"
ronaldo.liga="Profesional"
ronaldo.posicion="Delantero"
ronaldo.numero="7"
ronaldo.estadisticas="760 goles"
ronaldo.patrocinadores="Nike"

print(ronaldo.equipo)
print(ronaldo.habilidad)
print(ronaldo.edad)
print(ronaldo.genero)
print(ronaldo.nacionalidad)
print(ronaldo.liga)
print(ronaldo.posicion)
print(ronaldo.numero)
print(ronaldo.estadisticas)
print(ronaldo.patrocinadores)

ronaldo.correr()
ronaldo.patear()
ronaldo.proteger()
ronaldo.jugar()
ronaldo.vender()

