# Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
variable1 = float(input("Introduzca un número: "))
variable2 = float(input("Introduzca un número: "))

print("El cociente es:", variable1 / variable2)
print("El resto es:", variable1 % variable2)

if variable1 % 2 == 0:
    print(f"El dividendo {variable1} es PAR.")
else:
    print(f"El dividendo {variable1} es impar.")