def calcular_edad(dia_nacio,mes_nacio,anio_nacio,dia_actual,mes_actual,anio_actual):
   dias_nacio = (anio_nacio*12)*30 + (mes_nacio*30) + dia_nacio
   dias_actual = (anio_actual*12)*30 + (mes_actual*30) + dia_actual
   total = dias_actual - dias_nacio
   anios = total//360
   meses = (total%360)//30
   dias = (total%360)%30
   return str(anios) + ',' + str(meses) + ',' + str(dias)

print(calcular_edad(20,11,1986,16,10,1987))
