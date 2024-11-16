import math as m
def angulo_entre_agujas_reloj(hora, minutos):
    grados_x_hora = 360/12
    grados_x_hora_min = grados_x_hora/60
    grado_x_total_hora = (hora*grados_x_hora) + (minutos*grados_x_hora_min)
    grados_x_min = 360/60
    grado_x_total_minutos = grados_x_min*minutos
    return abs(grado_x_total_hora-grado_x_total_minutos)
print(angulo_entre_agujas_reloj(2,20))