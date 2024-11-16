def secuencia_de_fibonacci(fib1,fib2,fib3,fib4):
    if fib3 == fib1+fib2 and fib4 == fib3+fib2:
        return 'Fibofacil'
    else:
        return 'Fibofalsa'
print(secuencia_de_fibonacci(1,1,2,3))