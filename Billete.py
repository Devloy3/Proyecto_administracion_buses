class Billete:
       
       def __init__(self,id,persona,bus):
            self.__id = id
            self.__persona = persona
            self.__bus = bus 

       def SetBillete(self,id,persona,bus):
          self.__id = id
          self.__persona = persona
          self.__bus = bus 

       def GetBillete(self):
            return self.__id and self.__persona

       def GetBus(self):
            return self.__bus          

        
        
        
        
    


        

        

        
        




    






