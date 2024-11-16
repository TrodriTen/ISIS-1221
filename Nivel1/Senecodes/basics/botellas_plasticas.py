def calcular_pago_botellas(cant_pequenias:int, cant_grandes:int):
    pago_pequenias = cant_pequenias*0.1
    pago_grandes = cant_grandes*0.25
    return round(pago_pequenias + pago_grandes, 2)
print(calcular_pago_botellas(5,1))
