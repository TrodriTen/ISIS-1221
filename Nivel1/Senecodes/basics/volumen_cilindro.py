import math as m
def volumen_cilindro(radio, altura):
    area_circulo = m.pi*(radio**2)
    return round(area_circulo*altura, 1)
print(volumen_cilindro(1,1))