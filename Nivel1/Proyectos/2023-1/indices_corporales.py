def calcular_IMC(peso, altura):
    return round((peso/pow(altura,2)),2)

def calcular_porcentaje_grasa(peso,altura,edad,valor_genero):
    imc  = calcular_IMC(peso,altura)
    return round(1.2 * imc + 0.23 * edad - 5.4 - valor_genero,2)

def calcular_calorias_en_reposo(peso,altura,edad,valor_genero):
    return round((10*peso) + (6.25*altura) - (5*edad) + valor_genero,2)

def calcular_calorias_en_actividad(peso,altura,edad,valor_genero, valor_actividad):
    tmb = calcular_calorias_en_reposo(peso,altura,edad,valor_genero)
    return round(tmb*valor_actividad,2)

def consumo_calorias_recomendado_para_adelgazar(peso,altura,edad,valor_genero):
    tmb = calcular_calorias_en_reposo(peso,altura,edad,valor_genero)
    return round(tmb*(1-0.2),2), round(tmb*(1-0.15),2)