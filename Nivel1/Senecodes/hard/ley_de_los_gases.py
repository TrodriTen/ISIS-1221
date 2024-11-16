def calcular_moles(presion,volumen,temp_celcius):
    r = 8.314
    return (presion*(volumen/1000))/(r*(temp_celcius+273.15))
