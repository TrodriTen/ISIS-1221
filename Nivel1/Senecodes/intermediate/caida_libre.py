import math as m 
def velocidad_caida_libre(altura):
    return round(m.sqrt((2*9.8)*altura),2)
print(velocidad_caida_libre(1))