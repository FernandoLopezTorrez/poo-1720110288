class estudiante():
  
  escuela_perteneciente = None
  nivel_de_estudios= None
  edad = None
  nombre = None
  genero = None
  lugar_de_procedencia = None
  carrera_que_estudia = None
  horario = None
  matricula = None
  regularizado = None

  def __init__(self):
    print("Clase estudiante")
  
  def asistir (self):
    print ("Metodo asistir")

  def estudiar (self):
    print ("Metodo estudiar")

  def realizar_tareas (self):
    print ("Metodo realizar tareas")

  def honestidad_academica (self):
    print ("Metodo honestidad academica")
  
  def aprender (self):
    print ("Metodo aprender")

fernan = estudiante()
fernan.escuela_perteneciente = "Utec Tulancingo"
fernan.nivel_de_estudios = "Universitario"
fernan.edad = "20"
fernan.nombre = "Fernando Ismael Lopez Torrez"
fernan.genero = "Masculino"
fernan.lugar_de_procedencia = "Tulancingo, Hidalgo"
fernan.carrera_que_estudia = "Tecnologias de la información y la comunicación"
fernan.horario = "Matutino"
fernan.matricula = "1720110288"
fernan.regularizado = "si"

print(fernan.escuela_perteneciente)
print(fernan.nivel_de_estudios)
print(fernan.edad)
print(fernan.nombre)
print(fernan.genero)
print(fernan.lugar_de_procedencia)
print(fernan.carrera_que_estudia)
print(fernan.horario)
print(fernan.matricula)
print(fernan.regularizado)

fernan.asistir()
fernan.estudiar()
fernan.honestidad_academica()
fernan.realizar_tareas()
fernan.aprender()