def calcular_BMI(peso_lb, alt_inch):
    kg = peso_lb*0.45
    mts = alt_inch*0.025
    return round(kg/(mts**2),2)
print(calcular_BMI(1, 1))