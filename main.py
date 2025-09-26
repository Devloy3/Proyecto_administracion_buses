from Bus import Bus
from Billete import Billete
from Persona import Persona

buses = []
billetes = []


def crear_buses(): 
    numero = input("Numero del bus:")
    plazas = input("Plazas del bus:")
    bus = Bus(numero,plazas)
    bus1 = bus.GetBus()
    buses.append(bus1)

crear_buses()
