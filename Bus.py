class Bus:
    def __init__(self):
        self.__plazas = 100
        self.__Billetes_Vendidos = []

    def comprar_plaza(self,cantidad_de_billetes):
        self.__Billetes_Vendidos.append(cantidad_de_billetes)
        plaza_disponibles = self.__plazas - len(self.__Billetes_Vendidos)
        if plaza_disponibles <= 0:
            texto = f"No hay plazas"
            return texto
        else:
            texto_2 = f"Quedan {plaza_disponibles} disponibles"
            return texto_2
        
    
    def reembolsar_plazas(self):
        self.__Billetes_Vendidos.pop(1)
        plazas_disponibles = self.__plazas + len(self.__Billetes_Vendidos)
        if plazas_disponibles < 100:
            texto = f"Quedan {plazas_disponibles} plazas"
            return texto 
        elif plazas_disponibles == 100:
            texto_2 = f"Estan todas las plazas"
            return texto_2
    
    
    def mostrar_venta(self):
        print(f"Total: {self.__plazas}")
        print(f"Libre: {self.__plaza_disponible}")
        print(f"Vendido: {self.__plazas - self.__plaza_disponible }")
