def desperdicio_de_gaseosa(amigo1,amigo2,amigo3,capacidadBoton):
    if amigo1['capacidad_vaso'] - amigo1['capacidad_actual'] < capacidadBoton:
        return amigo1['nombre']
    elif amigo2['capacidad_vaso'] - amigo2['capacidad_actual'] < capacidadBoton:
        return amigo2['nombre']
    elif amigo3['capacidad_vaso'] - amigo3['capacidad_actual'] < capacidadBoton:
        return amigo3['nombre']
    else:
        return None
    

amigo_1 = {'nombre': 'Juan', 'capacidad_vaso': 100, 'capacidad_actual': 1.4}
amigo_2 = {'nombre': 'Candelaria', 'capacidad_vaso': 1000, 'capacidad_actual': 996}
amigo_3 = {'nombre': 'Milena', 'capacidad_vaso': 3.6, 'capacidad_actual': 2.5}
capacidad_boton = 4.5
print(desperdicio_de_gaseosa(amigo_1,amigo_2,amigo_3,capacidad_boton))