class Bus:
    def __init__(self):
        self.__plazas = 100
        self.__plaza_disponible = self.__plazas

    def comprar_plaza(self,cantidad_de_billetes):
        if self.__plaza_disponible >= cantidad_de_billetes:
            self.__plazas_disponible -= cantidad_de_billetes
            texto_2 = f"Quedan {self.__plaza_disponible} plazas"
            return texto_2
        else:
            texto = "No hay plazas, crack"
            return texto 
        
    def reembolsar_plazas(self,cantidad_de_billetes):
        if self.__plaza_disponible <= cantidad_de_billetes:
            self.__plazas_disponible += cantidad_de_billetes
            texto_2 = f"Hay{self.__plaza_disponible} plazas"
            return texto_2
        else:
            texto = "No hay plazas ha devolver, estupido"
            return texto 
        
