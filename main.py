from Bus import Bus
from Billete import Billete
from Persona import Persona

def menu():
        
        id = input("Numero del Bus:")
        plazas = input("Plazas del Bus:")
        bus = Bus()
        bus.Setnumero(id)
        bus.Setplazas(plazas)

        while True:
                print("<-- Menu -->")
                print("1.Ver los buses que hay")
                print("2.Comprar billetes")
        
        
                opcion = int(input("QUe haces:"))

                if opcion == 1:
                        numero = bus.Getnumero()
                        plaza = bus.Getplazas()
                        print(f"Esta el Bus {numero} y tiene {plaza}")
                elif opcion == 2: 
                        nombre = input("Nombre:")
                        apellidos = input("Apelldios:")
                        cantidad = 1 
                        persona = Persona()
                        persona.setNombre(nombre)
                        persona.setApellido(apellidos)
                        nombre2 = persona.getNombre()
                        apellido = persona.getApellido()

                        numero = bus.Getnumero()
                        bus.comprar_plaza(cantidad)
                        billete = Billete("B01",nombre2,apellido,numero)


        
menu()