def despacho_buses(personas_bus, personas_estacion):
    if personas_bus>=150 or personas_estacion>=40:
        return True
    else:
        return False
print(despacho_buses(50,200))