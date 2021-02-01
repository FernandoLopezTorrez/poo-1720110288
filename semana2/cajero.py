class cajero():

  instutucion_perteneciente = None
  modelo = None
  escala = None
  color = None
  capacidad = None
  tipo = None
  ubicacion = None
  seguridad = None
  admite_tarjetas = None
  pago_servicios = None

  def __init__(self):
    print("Clase Cajero automatico")

  def retirar (self):
    print("Metodo retirar ")

  def pagar_servicio(self):
    print("Metodo pagar servicio")

  def depositar (self):
    print("Metodo depositar")

  def facturacion (self):
    print("Metodo facturacion")

  def encender (self):
    print("Metodo encender")

cajero_bbva = cajero()
cajero_bbva.instutucion_perteneciente="BBVA"
cajero_bbva.modelo="2020"
cajero_bbva.escala="1.50m"
cajero_bbva.color="azul"
cajero_bbva.capacidad="500,000 pesos"
cajero_bbva.tipo="automatico"
cajero_bbva.ubicacion="Banco central"
cajero_bbva.seguridad="si"
cajero_bbva.admite_tarjetas="si"
cajero_bbva.pago_servicios="si"

print(cajero_bbva.instutucion_perteneciente)
print(cajero_bbva.modelo)
print(cajero_bbva.escala)
print(cajero_bbva.color)
print(cajero_bbva.capacidad)
print(cajero_bbva.tipo)
print(cajero_bbva.ubicacion)
print(cajero_bbva.seguridad)
print(cajero_bbva.admite_tarjetas)
print(cajero_bbva.pago_servicios)

cajero_bbva.encender()
cajero_bbva.retirar()
cajero_bbva.pagar_servicio()
cajero_bbva.depositar()
cajero_bbva.facturacion()