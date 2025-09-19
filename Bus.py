from Billete import billetes 

class bus:
    def __init__(self):
        self.billete = billetes()
        self.__plazas = 100

    def añadir_plaza(self):
        if self.billete:
            self.disponible = self.__plazas - 1
            
            if self.disponible == 0:
                print("Se acabaron las plazas")

    
        
