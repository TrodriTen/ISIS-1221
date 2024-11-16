def ordenar_enteros(num1,num2,num3):
    maximo = max(num1,num2,num3)
    minimo = min(num1,num2,num3)
    medio = num1 + num2 + num3 - minimo - maximo
    return str(maximo) + ',' + str(medio) + ',' + str(minimo)
print(ordenar_enteros(1,2,3))