#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10 
num1 = float(input("Introduce el primer número (entre 0 y 10): "))
num2 = float(input("Introduce el segundo número (entre 0 y 10): "))
if num1 >= 0 and num1 <= 10:
    if num2 >= 0 and num2 <= 10:
        if num1 > num2:
            print(f"El número {num1} es mayor que {num2}.")
        elif num1 < num2:
            print(f"El número {num1} es menor que {num2}.")
        else:
            print(f"Los números {num1} y {num2} son iguales.")   
    else:
        print("Número 2 no válido. Debe estar entre 0 y 10.")
else:
    print("Número 1 no válido. Debe estar entre 0 y 10.")
