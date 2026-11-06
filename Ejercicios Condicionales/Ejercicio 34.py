#Corrige los 4 errores o añade el código que necesites para que el siguiente programa se ejecute correctamente
import math
#inicializo valores a cada variable
var_numero="6734"
var_suma = 0
#obtengo su longitud
var_longitud=len(var_numero) 
#sumo cada digito a partir del índice de cada posición 
if var_longitud != 4:
    print("Fallo en el codigo")
else:
    var_suma = int(var_numero [1]) + int(var_numero [2])+ int(var_numero[3]) + (math.floor(int(var_numero)/1000))
    print(f"La suma es igual a {var_suma}")
#utilizo una condición y el operador aritmético % para saber si el resto da 0 y ver si es par 
if var_suma != 0:
    if var_suma % 2 == 0:
        print (f"El valor de {var_suma} es par")
    else:
        print (f"El valor de {var_suma} es impar")


        