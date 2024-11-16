def calcular_horario_llegada(hora_salida,minuto_salida,segundo_salida,duracion_horas,duracion_minutos,duracion_segundo):
    hora_salida_segundos = hora_salida*3600
    minuto_salida_segundos = minuto_salida*60
    duracion_horas_segundos = duracion_horas*3600
    duracion_minutos_segundos = duracion_minutos*60
    suma = hora_salida_segundos + duracion_horas_segundos + minuto_salida_segundos + duracion_minutos_segundos + segundo_salida + duracion_segundo
    hora_total = (suma//60)//60%24
    minutos_total = ((suma//60)%60)%60
    segundos_total = (suma%60)%60
    return str(hora_total) + ":" + str(minutos_total) + ":" + str(segundos_total)
print(calcular_horario_llegada(14,15,20,0,52,10))
