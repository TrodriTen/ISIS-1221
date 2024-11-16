def calcular_mediana(a,b,c):
    maximo = max(a,b,c)
    minimo = min(a,b,c)
    mediana = a+b+c-maximo-minimo
    return mediana
print(calcular_mediana(1,2,3))