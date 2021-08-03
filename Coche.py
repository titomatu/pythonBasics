class Coche:
    def __init__(self): #Constructor de la clase
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4 #Encapsulada, no se puede modificar desde fuera de la clase
        self.__enMarcha=False

    def arrancar(self):
        self.__enMarcha = True
    
    def estado(self):
        print("Tiene ruedas: ", self.__ruedas, " En marcha? ", self.__enMarcha)
    
    def __metodo_encapsulado(self):
        pass

#Instanciar una clase
micarro = Coche() 
micarro.arrancar()
#print("Cuántas ruedas tiene = ", micarro.__ruedas)
#AttributeError: 'Coche' object has no attribute '__ruedas'
micarro.__ruedas = 2
#No hace referencia a la misma vble dentro de la clase
print("Cuántas ruedas tiene = ", micarro.__ruedas)
micarro.estado()
