import math
def fahrenheitACelcius(grados):
    return round((grados-32)*(5/9),2)
print(fahrenheitACelcius(0))
def celciusAFahrenheit(grados):
    return (grados*(9/5))+32
print(celciusAFahrenheit(0))
def radianesAGrados(radianes):
    return (radianes*360)/(2*math.pi)
print(radianesAGrados(math.pi))
def gradosARadianes(grados):
    return (grados*2*math.pi)/(360)
print(gradosARadianes(90))
def invertirNum(num:int):
    numStr = str(num)
    return numStr[3] + numStr[2] + numStr[1] + numStr[0]
print(invertirNum(1234))