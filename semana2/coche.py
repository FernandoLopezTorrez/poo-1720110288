class coche():
  
  motor = None
  modelo = None
  traccion = None
  frenos  = None
  quemacocos = None
  color  = None
  aceleracion = None
  velocidad_maxima = None
  marca = None
  numero_llantas = None 

  def __init__(self):
    print("Clase coche")

  def acelerar (self):
    print("Metodo acelerar")

  def encender (self):
    print("Metodo encender")

  def frenar (self):
    print("Transportar")

  def girar (self):
    print("Metodo girar")

  def transportar (self):
    print("Metodo transportar")

tsuru = coche()
tsuru.motor="Modelo GA16DE de 16 Válvulas"
tsuru.modelo="2000"
tsuru.traccion="si"
tsuru.frenos="si"
tsuru.quemacocos="no"
tsuru.color="blanco"
tsuru.aceleracion="15km/m"
tsuru.velocidad_maxima="150km/h"
tsuru.marca="Nissan"
tsuru.numero_llantas="4"

print(tsuru.motor)
print(tsuru.modelo)
print(tsuru.traccion)
print(tsuru.frenos)
print(tsuru.quemacocos)
print(tsuru.color)
print(tsuru.aceleracion)
print(tsuru.velocidad_maxima)
print(tsuru.marca)
print(tsuru.numero_llantas)

tsuru.acelerar()
tsuru.frenar()
tsuru.girar()
tsuru.encender()
tsuru.transportar()