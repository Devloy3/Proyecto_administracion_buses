from Billete import Billete

class bus:
    def __init__(self,plazas):
        self.__plazas = plazas
        self.__plaza_disponible = self.__plazas
        Billetes_Vendidos = []

    def comprar_plaza(self,cantidad_de_billetes):
        if self.__plaza_disponible >= cantidad_de_billetes:
            self.__plazas_disponible -= 1
            texto_2 = f"Quedan {self.__plaza_disponible} plazas"
            return texto_2
        else:
            texto = "No hay plazas, crack"
            return texto 
        
    def reembolsar_plazas(self,cantidad_de_billetes):
        if self.__plaza_disponible <= cantidad_de_billetes:
            self.__plazas_disponible += 1
            texto_2 = f"Hay{self.__plaza_disponible} plazas"
            return texto_2
        else:
            texto = "No hay plazas ha devolver, estupido"
            return texto 
    
    def mostrar_venta(self):
        print(f"Total: {self.__plazas}")
        print(f"Libre: {self.__plaza_disponible}")
        print(f"Vendido: {self.__plazas - self.__plaza_disponible }")
