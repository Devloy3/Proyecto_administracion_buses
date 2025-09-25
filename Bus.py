from Billete import Billete

class bus:
    def __init__(self,plazas):
        self.__plazas = plazas
        self.__plaza_disponible = self.__plazas

    def comprar_plaza(self):
        if self.__plaza_disponible > 0:
            self.__plaza_disponible -= 1
            texto_2 = f"Quedan {self.__plaza_disponible} plazas"
            return texto_2
        else:
            texto = "No hay plazas, crack"
            return texto 
        
    def reembolsar_plazas(self):
        if self.__plaza_disponible < 100:
            self.__plaza_disponible += 1
            texto_2 = f"Hay{self.__plaza_disponible} plazas"
            return texto_2
        else:
            texto = "No hay plazas ha devolver, estupido"
            return texto 
    
    def mostrar_venta(self):
        print(f"Total: {self.__plazas}")
        print(f"Libre: {self.__plaza_disponible}")
        print(f"Vendido: {self.__plazas - self.__plaza_disponible }")
