class Vehiculo:
    def __init__(self, marca, modelo) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__enmarcha = False
        self.__acelero = False
    
    def arrancar(self):
        self.__enmarcha = True
        self.__acelero = True
    
    def estado(self):
        print("marca: ", self.__marca, " - modelo: ", self.__modelo)

class Moto(Vehiculo):
    pass

mimoto = Moto("Honda", "CBR")
mimoto.estado()