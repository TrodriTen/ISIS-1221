import indices_corporales as ic

def menu():
    print("Opciones de la calculadora de indicies corporales\n",
          "1. Calcular IMC\n",
          "2. Calcular porcentaje de grasa\n",
          "3. Calcular calorias en reposo\n",
          "4. Calcular calorias en actividad fisica\n",
          "5. Calcular calorias para adelgazar")
    opcion = int(input("Seleccione la opcion que desee: "))
    match opcion:
        case 1:
            imc = op1()
            print("Su IMC es de {0}".format(imc))
            menu()
        case 2:
            p_grasa = op2()
            print("Su porcentaje de grasa es de {0}".format(p_grasa))
            menu()
        case 3:
            cal_rep = op3()
            print("Sus calorias en reposo son de {0}".format(cal_rep))
            menu()
        case 4: 
            cal_act = op3()
            print("Sus calorias en actividad son de {0}".format(cal_act))
            menu()
        case 5:
            lim1, lim2 = op5()
            print("Sus calorias para adelgazar estan entre {0} y {1}".format(lim1, lim2))
            menu()
        case _:
            print("No eligio una opcion correcta")
            menu()
                    
def op1():
    peso = float(input("Introduzca su peso Kg: "))
    altura = float(input("Introduzca su altura M: "))
    return ic.calcular_IMC(peso,altura)

def op2():
    peso = float(input("Introduzca su peso Kg: "))
    altura = float(input("Introduzca su altura M: "))
    edad = int(input("Introduzca su edad: "))
    genero = input("Es hombre o mujer?: ")
    if genero.lower() == 'mujer':
        genero = 0
    elif genero.lower() == 'hombre':
        genero = 10.8 
    return ic.calcular_porcentaje_grasa(peso,altura,edad,genero)

def op3():
    peso = float(input("Introduzca su peso Kg: "))
    altura = float(input("Introduzca su altura M: "))
    edad = int(input("Introduzca su edad: "))
    genero = input("Es hombre o mujer?: ")
    if genero.lower() == 'mujer':
        genero = -161
    elif genero.lower() == 'hombre':
        genero = 5
    return ic.calcular_calorias_en_reposo(peso,altura,edad,genero)

def op4():
    peso = float(input("Introduzca su peso Kg: "))
    altura = float(input("Introduzca su altura M: "))
    edad = int(input("Introduzca su edad: "))
    genero = input("Es hombre o mujer?: ")
    actividad = int(input("Introduzca su actividad fisica\n"
                            "1. poco\n",
                            "2. ligero\n", 
                            "3. moderado\n",
                            "4. deportista\n",
                            "5. atleta"))
    if genero.lower() == 'mujer':
        genero = -161
    elif genero.lower() == 'hombre':
        genero = 5
    match actividad:
        case 1:
            actividad = 1.2
        case 2:
            actividad = 1.375
        case 3:
            actividad = 1.55
        case 4:
            actividad = 1.725
        case 5:
            actividad = 1.9
        case __:
            print("No digito un numero para su actividad fisica!")
            op4()
    return ic.calcular_calorias_en_actividad(peso,altura,edad,genero,actividad)

def op5():
    peso = float(input("Introduzca su peso Kg: "))
    altura = float(input("Introduzca su altura M: "))
    edad = int(input("Introduzca su edad: "))
    genero = input("Es hombre o mujer?: ")
    if genero.lower() == 'mujer':
        genero = -161
    elif genero.lower() == 'hombre':
        genero = 5
    return ic.consumo_calorias_recomendado_para_adelgazar(peso,altura,edad,genero)

menu()
    
