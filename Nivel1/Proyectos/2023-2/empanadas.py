def calcular_costo_empanadas(precio_carne, precio_papa,precio_aceite):
    return round((2.5*precio_carne + 3*precio_papa + precio_aceite)/50,2)

def calcular_tiempo_coccion_lote_empanadas(tiempo, cantidad):
    return tiempo*cantidad

def calcular_rentabilidad(precio_carne, precio_papa,precio_aceite,precio_venta):
    costo = calcular_costo_empanadas(precio_carne,precio_papa,precio_aceite)
    return precio_venta - costo

def calcular_cantidad_empanadas_meta(precio_carne, precio_papa,precio_aceite,precio_venta, empleados, arriendo):
    rentabilidad = calcular_rentabilidad(precio_carne,precio_papa,precio_aceite,precio_venta)
    return int((arriendo + empleados*45000)/rentabilidad)

def calcular_precio_venta_promocion(precio_unidad, cantidad):
    return round(((cantidad//5) * 3 + (cantidad%5))* precio_unidad,2)