def filtro_ternario(cantidad_carros,numero_carro):
    if 1 <= numero_carro <= (cantidad_carros/3):
        return 1
    elif (cantidad_carros/3)+1 <= numero_carro <= 2*(cantidad_carros/3):
        return 2
    else:
        return 3
# Casos de prueba
print(filtro_ternario(9, 1))  # Esperado: Primer lote
print(filtro_ternario(9, 4))  # Esperado: Segundo lote
print(filtro_ternario(9, 7))  # Esperado: Tercer lote
print(filtro_ternario(6, 3))  # Esperado: Primer lote
print(filtro_ternario(6, 6))  # Esperado: Tercer lote
print(filtro_ternario(12, 8)) # Esperado: Segundo lote
print(filtro_ternario(12, 12))# Esperado: Tercer lote
