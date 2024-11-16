def calcular_tarifa_taxi(km_recorridos):
    total_distancia = ((km_recorridos*1000)/100)*82
    return 4000 + total_distancia
print(calcular_tarifa_taxi(1))