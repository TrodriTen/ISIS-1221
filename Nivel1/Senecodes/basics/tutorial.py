def saludo_personalizado(nombre:str, materia:str):
    return 'Hola estudiante ' + nombre + ', Bienvenido a la materia de ' + materia
x = saludo_personalizado('Manuel', 'Programacion')
print(x)