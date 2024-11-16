import math as m
def area_poligono_regular(num_lados, longitud):
    return round((num_lados*(longitud**2))/(4*m.tan(m.pi/num_lados)),2)
print(area_poligono_regular(4,2))
