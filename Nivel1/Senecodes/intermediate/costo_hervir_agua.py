def costo_hervir_agua(masa_agua):
    return round((((masa_agua*4186*80)/3600)/1000)*0.089,4)
print(costo_hervir_agua(50))