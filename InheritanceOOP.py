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
    __hcaballito = ""

    def hcaballito(self):
        self.__hcaballito = "Voy a hacer el caballito"
    
    #Sobreescritura de métodos
    def estado(self):
        print("Vas a hacer el caballito?? ", self.__hcaballito)

class VehiculoE:
    def __init__(self):
        self.__autonomia = 100
    
    def cargar(self):
        self.__cargando = True
    
    def estado(self):
        print("Carga: " , self.__cargando, " - Autonomia: ", self.__autonomia)

#Herencia Múltiple
#Se le da preferencia a la primera clase que está en el paréntesis
class BicicletaE(VehiculoE, Vehiculo):
    def __init__(self, marca, modelo) -> None:
        super().__init__()
        self.__marca = marca
        self.__modelo = modelo
    
    def estado(self):
        super().estado()
        print("Marca: ", self.__marca)

mimoto = Moto("Honda", "CBR")
mimoto.hcaballito()
mimoto.estado()

#Herencia Múltiple
bicie = BicicletaE("Tern", "D16")
bicie.cargar()
bicie.estado()

print(isinstance(bicie, VehiculoE))