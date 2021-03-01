class asistencias:
  FaltasTotales= 0
  
  def __init__(self):
    pass

  def calcular (self):
    repetir = "s"
    retardos = 0
    while repetir == "s":
      materia = input("Introduze el nombre de la materia: ")
      NombreAlumno = input("Introduce el nombre del alumno: ")
      NumeroClases = int(input("Introduce la cantidad de clases: "))
      NumeroFaltas = int(input("Introduce la cantidad de faltas: "))
      retardos = int(input("Introduce la cantidad de retardos: "))
      print("materia: ", materia)
      print("Alumno: ", NombreAlumno)
      print("Numero de clases:  ", NumeroClases)
      print("Numero de faltas: ", NumeroFaltas)
      print("Numero de retardos: ", retardos)
      retardos = retardos // 3 
      NumeroFaltas = NumeroFaltas + retardos
      porcentaje = (NumeroFaltas*100) / NumeroClases
      print("Porcentaje de asistencias: " , 100 - porcentaje)
      if 100 - porcentaje <= 80:
        print ("No tiene derecho")
      else :
        print ("tiene derecho")
      repetir = input("Otra evaluación? s/n ")

porcentaje=asistencias()
porcentaje.calcular()

      






