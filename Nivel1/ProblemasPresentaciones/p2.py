def rotar(x1,x2,x3):
    temp = x2
    x2 = x1
    x1 = x3
    x3 = temp  
    return x1,x2,x3
print(rotar(1,2,3))
def intereses():
    pesos = float(input('Ingrese su cantidad a invertir: '))
    i = float(input('Ingrese la tasa de interes a invertir: '))
    n = int(input('Ingrese numero de peridodos de la inversion: '))
    return round(pesos*(pow(1+(i/100),n)),2)
print(intereses())