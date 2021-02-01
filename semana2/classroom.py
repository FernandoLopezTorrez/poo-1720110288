class plataforma():

  tablon_tareas = None
  notificaciones = None
  clases = None
  modos = None
  mensajes = None
  evaluaciones = None
  programacion_actividades  = None
  calendario = None
  ajustes = None

  def __init__(self):
    print("Clase plataforma")

  def programar_clases (self):
    print("Metodo programar clases")

  def mensajeria (self):
    print("Metodo mensajeria")

  def calificar (self):
    print("Metodo calificar")

  def enviar_archivos(self):
    print("Metodo enviar archivos")

  def perzonalizar(self):
    print("Metodo perzonalizar")

classroom = plataforma()
classroom.tablon_tareas="si"
classroom.notificaciones="si"
classroom.clases="si"
classroom.modos="si"
classroom.mensajes="si"
classroom.evaluaciones="si"
classroom.programacion_actividades="si"
classroom.calendario="si"
classroom.ajustes="si"

print(classroom.tablon_tareas)
print(classroom.notificaciones)
print(classroom.clases)
print(classroom.modos)
print(classroom.mensajes)
print(classroom.evaluaciones)
print(classroom.programacion_actividades)
print(classroom.calendario)
print(classroom.ajustes)

classroom.programar_clases()
classroom.mensajeria()
classroom.calificar()
classroom.enviar_archivos()
classroom.perzonalizar()




