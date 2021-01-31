class serie():
  
  canal = None
  horario = None
  genero = None
  audiencia_objetivo = None
  animado = None
  reparto = None
  presupuesto = None
  publicidad = None
  en_vivo = None
  duracion = None

  def __init__(self):
    print ("Clase Serie de TV")

  def entretener (self):
    print("Metodo entretener")

  def informar (self):
    print("Metodo informar")

  def presentar (self):
    print("Metodo presentar")

  def vender (self):
    print("Metodo vender")
  
  def concursar (self):
    print ("Metodo concursar")

  
reallity = serie ()
reallity.canal="5"
reallity.horario="12:00 a 01:00"
reallity.genero="Reallity show"
reallity.audiencia_objetivo="Adolecentes"
reallity.animado="No"
reallity.reparto="pepe el toro"
reallity.presupuesto="5 pesos"
reallity.publicidad="si"
reallity.en_vivo="no"
reallity.duracion="Un hora"

print(reallity.canal)
print(reallity.horario)
print(reallity.genero)
print(reallity.audiencia_objetivo)
print(reallity.animado)
print(reallity.reparto)
print(reallity.presupuesto)
print(reallity.publicidad)
print(reallity.en_vivo)
print(reallity.duracion)

reallity.entretener()
reallity.informar()
reallity.presentar()
reallity.vender()
reallity.concursar()
