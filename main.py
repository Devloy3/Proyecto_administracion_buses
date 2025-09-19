print("Ingrese el número de asientos")
asientos_totales = int(input())
asientos_ocupados = 0
asientos_libres = []
entradas_vendidas = 0

def iniciar_asientos():
    for i in range(asientos_totales):
        asientos_libres.append(0)  # 0 = libre, 1 = ocupado

def borrar_lista():
    for i in range(asientos_totales):
        asientos_libres[i] = 0

def validacion_opcion(num):
    if 0 <= num <= 3:
        return num
    else:
        print("Error")
        return -1  # devuelve algo para evitar errores

def mostrar_menu():
    print("""1.- Venta de billetes.
2.- Devolución de billetes.
3.- Estado de la venta.
0.- Salir.""")
    

def venta_entradas(entradas):
    for i in range(entradas):
        asientos_libres[i] = 1
        

def devolucion_entradas(devolucion):
    global entradas_vendidas 
    entradas_vendidas-= devolucion
    if entradas_vendidas >= 0:
        borrar_lista()
        venta_entradas(entradas_vendidas)
        print("Se devolvieron {} billetes".format(devolucion))
    else:
        print("Error")
        entradas_vendidas += devolucion  # revertimos

# Programa principal
iniciar_asientos()
opcion_selecionada = -1

mostrar_menu()
while opcion_selecionada != 0:
    #print("Mapa de asientos: {}".format(asientos_libres))
    opcion_selecionada = validacion_opcion(int(input("")))
    
    if opcion_selecionada == 0:
        print("")
    elif opcion_selecionada == 1:
        numero_venta = int(input(""))
        entradas_vendidas += numero_venta
        if entradas_vendidas <= asientos_totales:
            #print("Entradas vendidas: {}".format(entradas_vendidas))
            venta_entradas(entradas_vendidas)
            print("Se vendieron {} billetes".format(numero_venta))
        else:
            #print("No hay suficientes asientos disponibles. Solo quedan: {}".format(asientos_totales - (entradas_vendidas - numero_venta)))
            entradas_vendidas -= numero_venta
    elif opcion_selecionada == 2:
        devolucion = int(input(""))
        devolucion_entradas(devolucion)
    elif opcion_selecionada == 3:
        print("Total: {}".format(asientos_totales))
        print("Libre: {}".format(asientos_totales - entradas_vendidas))
        print("Vendido: {}".format(entradas_vendidas))
    else:
        print("Error")