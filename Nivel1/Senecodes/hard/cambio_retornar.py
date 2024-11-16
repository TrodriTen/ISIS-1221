def calcular_cambio(cambio):
    m1 = cambio//500
    m2 = (cambio%500)//200
    m3 = ((cambio%500)%200)//100
    m4 = (((cambio%500)%200)%100)//50
    return str(m1) + ',' + str(m2) + ',' + str(m3) + ',' + str(m4)
print(calcular_cambio(850))
