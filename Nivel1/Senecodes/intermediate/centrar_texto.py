def centrar_texto(cadena, ancho_terminal):
    longitud_cadena = len(cadena)
    espacios_inicio = (ancho_terminal-longitud_cadena)//2
    return '.'*espacios_inicio + cadena
print(centrar_texto('abc', 10))
