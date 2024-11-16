import random as r
def llave_secreta(p,g,b):
    a = r.randint(0,p-1)
    b_gen = (pow(g,a))%p
    k = (pow(b,a))%p
    return  "El b generado es {0} La llave simétrica es {1}".format(b_gen,k)
print(llave_secreta(5,10,3))