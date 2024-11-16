def saludar_repetidas_veces(nombre, veces):
    mitad = veces//2
    return ('H'+ ('o'*veces) + 'l' + ('a'*mitad) + ' ' + nombre)
print(saludar_repetidas_veces('Egan', 5))