import math as m
def area_triangulo(s1,s2,s3):
    s = (s1+s2+s3)/2
    return round(m.sqrt(s*(s-s1)*(s-s2)*(s-s3)),1)
print(area_triangulo(1,1,1))