class Persona:
    def __init__(self, nombre, edad, lugar_residencia):
        self.__nombre = nombre
        self.__edad = edad
        self.__lugar_residencia = lugar_residencia
    
    def descripcion(self):
        print("Nombre: ", self.__nombre, " Edad: ", self.__edad, " Residencia: ", self.__lugar_residencia)

class Empleado(Persona):
    def __init__(self, nombre, edad, lugar_residencia, salario, antiguedad):
        super().__init__(nombre, edad, lugar_residencia)
        self.__salario = salario
        self.__antiguedad = antiguedad

ricky = Empleado("Ricky", 37, "Vancouver", 8000, 15)
ricky.descripcion()