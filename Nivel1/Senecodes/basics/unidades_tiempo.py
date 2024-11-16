def tiempo_a_segundos(dias, horas, min, seg):
    seg_dias = (((dias*24)*60)*60)
    seg_hor = ((horas*60)*60)
    seg_min = (min*60)
    return seg + seg_dias + seg_hor + seg_min
print(tiempo_a_segundos(1,0,0,0))