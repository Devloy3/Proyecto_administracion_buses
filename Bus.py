class Bus:
    def __init__(self,id,plazas):
        self.__plazas = plazas
        self.__Billetes_Vendidos = []
        self.__numero = id 

    def Setnumero(self,id):
        self.__numero = id

    def Getnumero(self):
        return self.__numero
    
    def Setplazas(self,plazas):
        self.__plazas = plazas

    def Getplazas(self):
        return self.__plazas

    def comprar_plaza(self,cantidad_de_billetes):
            self.__Billetes_Vendidos.append(cantidad_de_billetes)
            plaza_disponibles = self.__plazas - len(self.__Billetes_Vendidos)
            if plaza_disponibles <= 0:
                texto = f"No hay plazas"
                return texto
            else:  
                return plaza_disponibles
    
    def reembolsar_plazas(self):
        self.__Billetes_Vendidos.pop(1)
        plazas_disponibles = self.__plazas + len(self.__Billetes_Vendidos)
        if plazas_disponibles < 100:
            return plazas_disponibles 
        elif plazas_disponibles == 100:
            texto_2 = f"Estan todas las plazas"
            return texto_2
