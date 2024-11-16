def precio_minimo(p1,p2):
    menor = (p1+p2 - abs(p1-p2))//2
    return menor
print(precio_minimo(1989,1987))