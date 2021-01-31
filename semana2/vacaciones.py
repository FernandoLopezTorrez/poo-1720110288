class vacaciones():

  temporada = None
  alojamiento = None
  internacionales = None
  nacionales = None
  duracion = None
  transporte = None
  equipaje = None
  comida = None
  recreacion = None
  itinerario = None

  def __init__(self):
    print("Clase vacaciones")
  
  def viajar (self):
    print("Metodo viajar")
    
  def descansar (self):
    print("Metodo descansar")

  def conocer(self):
    print("Metodo conocer")
  
  def relajar (self):
    print("Metodo relajar")

  def comer (self):
     print("Metodo comer")
  

verano = vacaciones()
verano.temporada = "Verano"
verano.alojamiento="Hotel"
verano.internacionales="Si"
verano.duracion="2 semanas"
verano.transporte="Avión"
verano.equipaje="Maletas"
verano.comida="Mucha"
verano.recreacion="Si"
verano.itinerario="si"

print(verano.temporada)
print(verano.alojamiento)
print(verano.internacionales)
print(verano.duracion)
print(verano.transporte)
print(verano.equipaje)
print(verano.comida)
print(verano.recreacion)
print(verano.itinerario)


verano.viajar()
verano.conocer()
verano.descansar()
verano.relajar()
verano.comer()