#Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
if num1 > num2:
    print(f"El número {num1} es mayor que {num2}.")
elif num1 < num2: #Uso el else-if (elif) para poner un else y un condicional extra, he hecho como en makecode
    print(f"El número {num1} es menor que {num2}.")
else:
    print(f"Los números {num1} y {num2} son iguales.")