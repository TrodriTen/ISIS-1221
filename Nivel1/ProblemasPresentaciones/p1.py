def monedas(total):
    nikel = 5
    dime = 10
    total = total*100
    if(total%dime == 0):
        return total/dime
    else:
        numDimes = total//dime
        temp = total - (dime*numDimes)
        numNikel = temp//nikel
        return numDimes + numNikel

print(monedas(1.35))

