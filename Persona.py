class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def setPersona(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def getPersona(self):
        return self.__nombre and self.__apellido
    



