from Persona import Persona
from Bus import Bus

class Billete:

    def __init__(self,cantidad=1):
        self.__NombreYApellido = Persona()
        self.bus = Bus()
        self.bus.comprar_plaza(cantidad)

    def set(self,Nombre,Apellido):
        self.__NombreYApellido.setNombre(Nombre)
        self.__NombreYApellido.setApellido(Apellido)

        

        
        




    






