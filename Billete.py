from Persona import Persona

class Billete:

    def __init__(self, Nombre, Apellido):
        self.__NombreYApellido = Persona(Nombre, Apellido)

    def setNombre_Y_Apellido(self, nombre, apellido):
        self.__NombreYApellido.setNombre(nombre)
        self.__NombreYApellido.setApellido(apellido)

    def getNombre(self):
        return self.__NombreYApellido.getNombre()

    def getApellido(self):
        return self.__NombreYApellido.getApellido()
