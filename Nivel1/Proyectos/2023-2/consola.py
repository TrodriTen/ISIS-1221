import empanadas as em

def menu():
    print("Opciones de la calculadora de indicies corporales\n",
          "1. Calcular costo empanada\n",
          "2. Calcular tiempo coccion lote\n",
          "3. Calcular rentabilidad\n",
          "4. Calcular meta empanadas\n",
          "5. Calcular precio venta promocion")
    opcion = int(input("Seleccione la opcion que desee: "))
    match opcion:
        case 1:
            costo = op1()
            print("El costo de la empanada es de {0}".format(costo))
            menu()
        case 2:
            tiempo = op2()
            print("El tiempo coccion lote es de {0}".format(tiempo))
            menu()
        case 3:
            rent = op3()
            print("La rentabilidad es de {0}".format(rent))
            menu()
        case 4: 
            meta = op4()
            print("La meta de empanadas es de {0}".format(meta))
            menu()
        case 5:
            promo, cantidad = op5()
            print("El precio de venta en promoción de {0} empanadas seria de $ {1}".format(cantidad,promo))
            menu()
        case _:
            print("No eligio una opcion correcta")
            menu()
                    
def op1():
    precio_carne = int(input("Introduzca el precio de la carne: "))
    precio_papa = int(input("Introduzca el precio de la papa: "))
    precio_aceite = int(input("Introduzca el precio del aceite: "))
    return em.calcular_costo_empanadas(precio_carne,precio_papa,precio_aceite)

def op2():
    tiempo = int(input("Introduzca el tiempo en segundos que tarda una empanada: "))
    cantidad = int(input("Introduzca la cantidad de empanadas a hacer: "))
    return em.calcular_tiempo_coccion_lote_empanadas(tiempo,cantidad)

def op3():
    precio_carne = int(input("Introduzca el precio de la carne: "))
    precio_papa = int(input("Introduzca el precio de la papa: "))
    precio_aceite = int(input("Introduzca el precio del aceite: "))
    precio_venta = float(input("Introduzca el precio de venta de una empanada: "))
    return em.calcular_rentabilidad(precio_carne,precio_papa,precio_aceite,precio_venta)

def op4():
    precio_carne = int(input("Introduzca el precio de la carne: "))
    precio_papa = int(input("Introduzca el precio de la papa: "))
    precio_aceite = int(input("Introduzca el precio del aceite: "))
    precio_venta = float(input("Introduzca el precio de venta de una empanada: "))
    arriendo = float(input("Ingrese el valor del arriendo por dia: "))
    empleados = int(input("Introduzca el numero de empleados: "))
    return em.calcular_cantidad_empanadas_meta(precio_carne,precio_papa,precio_aceite,precio_venta,empleados,arriendo)

def op5():
    venta_unidad = int(input("Introduzca el precio de una empanada: "))
    cantidad = int(input("Introduzca la cantidad de empanadas a hacer: "))
    return em.calcular_precio_venta_promocion(venta_unidad, cantidad), cantidad

menu()
    
