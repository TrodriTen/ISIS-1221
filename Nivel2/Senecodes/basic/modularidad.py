def es_divisible(n,d):
    if n%(2*d) == 0:
        return 2
    elif n%d == 0:
        return 1
    else:
        return 0
    