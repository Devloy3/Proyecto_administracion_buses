class Bus:
    def __init__(self,numero,plazas):
        self.__plazas = plazas
        self.__numero = numero
        self.__plazas_ocupadas = []

    def SetBus(self,numero,plazas):
        self.__numero = numero
        self.__plazas = plazas

    def GetBus(self):
        return self.__numero and self.__plazas
    
    def asignar_plaza(self,cantidad_de_billetes):
            self.__plazas_ocupadas.append(cantidad_de_billetes)
            plaza_disponibles = self.__plazas - len(self.__plazas_ocupadas)
            if plaza_disponibles <= 0:
                texto = f"No hay plazas"
                return texto
            else:  
                return plaza_disponibles
    
    def reembolsar_plazas(self):
        self.__plazas_ocupadas.pop(1)
        plazas_disponibles = self.__plazas + len(self.__plazas_ocupadas)
        if plazas_disponibles < 100:
            return plazas_disponibles 
        elif plazas_disponibles == 100:
            texto_2 = f"Estan todas las plazas"
            return texto_2
