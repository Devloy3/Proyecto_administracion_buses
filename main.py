from Menu import Menu
from Bus import bus

Bus1 = bus(100)

compra = Menu()

compra.inicio()

opcion = None

while opcion != 0:
    compra.mostrar_menu()
    int(input("Selecciona una opcion: "))
    if opcion == 1:
        Bus1.comprar_plaza()
    elif opcion == 2:
        Bus1.reembolsar_plazas()
    elif opcion == 3:
        Bus1.mostrar_venta()
    











