class calculadora():

  marca = None
  modelo = None
  cientifica = None
  grafica = None
  escala = None
  color = None
  botones = None
  programable = None
  fisica = None
  virtual = None

  def __init__(self):
    print("Clase calculadora")

  def sumar (self):
    print("Metodo suma")
  
  def resta (self):
    print("Metodo resta")

  def multiplicacion (self):
    print("Metodo multiplicacion")

  def division (self):
    print("Metodo división")

  def graficar (self):
    print("Metodo graficar")

cientifica = calculadora()
cientifica.marca="cassio"
cientifica.modelo="9000"
cientifica.grafica="no"
cientifica.escala="mediana"
cientifica.color="negra"
cientifica.botones="de plastico"
cientifica.programable="no"
cientifica.fisica="si"
cientifica.virtual="no"

print(cientifica.marca)
print(cientifica.modelo)
print(cientifica.grafica)
print(cientifica.escala)
print(cientifica.color)
print(cientifica.botones)
print(cientifica.programable)
print(cientifica.fisica)
print(cientifica.virtual)

cientifica.sumar()
cientifica.resta()
cientifica.multiplicacion()
cientifica.division()
cientifica.graficar()