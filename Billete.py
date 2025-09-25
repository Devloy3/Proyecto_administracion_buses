from Persona import Persona
from Bus import Bus

class Billete:

    def __init__(self,nombre,apellido,cantidad=1):
        self.__NombreYApellido = Persona()
        self.__NombreYApellido.setNombre(nombre)
        self.__NombreYApellido.setApellido(apellido)
        self.__bus = Bus()
        self.__bus.comprar_plaza(cantidad)

    def __str__(self):
        self.__NombreYApellido.getNombre()
        self.__NombreYApellido.getApellido()
        print(f"La persona con {self.__NombreYApellido.getNombre()} y apellido {self.__NombreYApellido.getApellido()} tiene una plaza")

        

        
        




    






