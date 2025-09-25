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
        nombre = self.__NombreYApellido.getNombre()
        apellido = self.__NombreYApellido.getApellido()
        bus = self.__bus.Getnumero()
        texto = f"La persona {nombre}{apellido} ha comprado en el bus en {bus} "

        

        

        
        




    






