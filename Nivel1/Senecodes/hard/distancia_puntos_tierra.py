import math as m
def calcular_distancia_tierra(t1,g1,t2,g2):
    return round(6371.01 * m.acos((m.sin(m.radians(t1))*m.sin(m.radians(t2))) + (m.cos(m.radians(t1))*m.cos(m.radians(t2))*m.cos(m.radians(g1-g2)))),2)
print(calcular_distancia_tierra(4.624335, -74.063644, 10.963889, -74.796387 ))