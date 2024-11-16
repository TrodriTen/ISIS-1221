def calcular_tiempo_descarga(velocidad, tamanio_archivo):
    velocidad_MB = velocidad/8
    tamanio_archivo_MB = tamanio_archivo*1000
    return round(tamanio_archivo_MB/velocidad_MB)
print(calcular_tiempo_descarga(10,10))
    
    