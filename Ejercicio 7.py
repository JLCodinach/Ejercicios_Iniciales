# Programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales? 
variable1 = float(input("Introduce un número: "))
variable2 = float(input("Introduce un número: "))

resultadosuma=(variable1 + variable2)
resultadoresta=(variable1 - variable2)
resultadomultiplicacion=(variable1 * variable2)
resultadoexponente=(variable1 ** variable2)

if variable2 == 0:
    print("No se puede dividir entre 0.")
    print("La suma es: ", resultadosuma)
    print("La resta es: ", resultadoresta)
    print("La multiplicación es: ", resultadomultiplicacion)
    print("El exponente es: ", resultadoexponente)
else:
    variable3 = round(variable1 / variable2, 2)
    resultadodivisionentera = (variable1 // variable2)
    print("La suma es: ", resultadosuma)
    print("La resta es: ", resultadoresta)
    print("La multiplicación es: ", resultadomultiplicacion)
    print("La división es: ", variable3)
    print("La división entera es: ", resultadodivisionentera)
    print("El exponente es: ", resultadoexponente)