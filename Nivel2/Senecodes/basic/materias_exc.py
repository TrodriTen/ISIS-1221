def conteo_buenas_notas(notas):
    conteo = 0
    if notas['Matematica'] > 4.0:
        conteo +=1
    if notas['Ingles'] > 4.0:
        conteo +=1  
    if notas['Sociales'] > 4.0:
        conteo +=1  
    if notas['Ciencias'] > 4.0:
        conteo +=1  
    if notas['Deportes'] > 4.0:
        conteo +=1  
    return conteo
notas = {'Matematica': 3.0, 'Ingles': 1.0, 'Sociales': 5.0, 'Ciencias': 4.0, 'Deportes': 3.5} 
print(conteo_buenas_notas(notas))