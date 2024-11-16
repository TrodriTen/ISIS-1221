def potenciador(x,n):
    if n == 1 or n ==0:
        return False
    i = pow(x,1/n)
    if i**n == x:
        return True
    return False

