class avion():
  
  nombre = None
  empresa_fabricante = None
  valor = None
  modelo  = None
  capacidad  = None
  dormitorio = None
  internet = None
  comunicaciones = None
  escala_largo = None
  escala_alto  = None

  def __init__(self):
    print ("Clase Avión")
  
  def despegar (self):
    print ("Metodo despegar")
  
  def volar (self):
    print ("Metodo volar")

  def aterrizar (self):
    print ("Metodo aterrizar")

  def transportar (self):
    print ("Metodo transportar")

  def comunicar (self):
    print ("Metodo comunicar")

avion_presidencial = avion()
avion_presidencial.nombre ="José María Morelos y Pavón"
avion_presidencial.empresa_fabricante ="Boeing"
avion_presidencial.valor="218.7 millones de dólares"
avion_presidencial.modelo="modelo 787-8"
avion_presidencial.capacidad="80 pasajeros"
avion_presidencial.dormitorio="si"
avion_presidencial.internet="si"
avion_presidencial.comunicaciones="si"
avion_presidencial.escala_largo="60 metros"
avion_presidencial.escala_alto="17 metros"

print(avion_presidencial.nombre)
print(avion_presidencial.empresa_fabricante)
print(avion_presidencial.modelo)
print(avion_presidencial.valor)
print(avion_presidencial.capacidad)
print(avion_presidencial.dormitorio)
print(avion_presidencial.internet)
print(avion_presidencial.comunicaciones)
print(avion_presidencial.escala_alto)
print(avion_presidencial.escala_largo)

avion_presidencial.despegar()
avion_presidencial.volar()
avion_presidencial.aterrizar()
avion_presidencial.transportar()
avion_presidencial.comunicar()

