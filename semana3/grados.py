class grados():
    def _init_(self):
        pass
    
    def cantidad(self):
        print("Introduzca la cantidad de temperaturas a promediar: ")
        cantidadDeTemperaturas = int(input())
        sumaTemperaturasF = 0
        
        for i in range(cantidadDeTemperaturas):
            print("Introduce la cantidad " + str(i +1)+ ":")
            sumaTemperaturasF = sumaTemperaturasF + ((int(input()) * (1.8)) + 32)
        print("El promedio de las temperaturas en Farenheit es:")
        print(sumaTemperaturasF / cantidadDeTemperaturas)
        
x = grados()
x.cantidad()


