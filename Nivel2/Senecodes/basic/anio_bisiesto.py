def anio_bisesto(anio):
    if anio%100 == 0 and anio%400 != 0:
        return False
    elif anio%4 == 0:
        return True
    else: 
        return False