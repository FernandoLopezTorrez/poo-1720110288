class banco():

  institucion_perteneciente = None
  cajero_automatico = None
  atencion_cliente = None
  personal = None
  sala_de_espera = None
  escala  = None
  cajas = None
  escaleras = None
  banca_movil = None
  prestamos = None
 
  
  def __init__(self):
    print("Clase banco.")
  
  def invertir (self):
    print("Metodo invertir")
    
  def prestar (self):
    print("Metodo prestar")
    
  def administrar (self):
    print("Metodo administrar")
    
  def  financiar (self):
    print("Metodo financiarr")
    
  def asesorar (self):
    print("Metodo asesorar")


bbva = banco()
bbva.institucion_perteneciente = "BBVA"
bbva.cajero_automatico = "si"
bbva.atencion_cliente = "si"
bbva.personal = "si"
bbva.sala_de_espera = "si"
bbva.escala = "Dos pisos"
bbva.cajas = "si"
bbva.escaleras = "si"
bbva.banca_movil = "si"
bbva.prestamos = "si"

print(bbva.institucion_perteneciente)
print(bbva.cajero_automatico)
print(bbva.atencion_cliente)
print(bbva.personal)
print(bbva.sala_de_espera)
print(bbva.escala)
print(bbva.cajas)
print(bbva.escaleras)
print(bbva.banca_movil)
print(bbva.prestamos)

bbva.administrar()
bbva.asesorar()
bbva.financiar()
bbva.invertir()
bbva.prestar()