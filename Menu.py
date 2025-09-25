class Menu:

    def inicio(self ):
        nombre = input("Entre su nombre por favor: ")
        apellido= input("Ahora su apellido por favor su nombre por favor: ")
        return print(f"Bienvenido  {nombre} {apellido}  ¿En que le podemos ayudar?")
    
    def mostrar_menu(self ): 
        print("""1.- Venta de billetes.
        2.- Devolución de billetes.
        3.- Estado de la venta.
        0.- Salir.""") 
        
    
   
