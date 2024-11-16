def convertir_eficiencia_combustible(millas_por_galon):
    return round(((3.78/(millas_por_galon*1.6)))*100,2)
print(convertir_eficiencia_combustible(10))