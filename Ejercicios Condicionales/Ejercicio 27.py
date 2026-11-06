# Mejora el programa anterior para comprobar que el valor introducido es una letra.
letra = input("Introduce una letra: ")

if letra.isdigit()==True:
    print("El valor introducido es un número.")
elif len(letra) != 1 or letra.isalpha()==False:
    print("La letra es mayúscula ¿?")
else:
    if letra.isupper()==True:
        print("La letra es mayúscula.")
    elif letra.islower()==True:
        print("La letra es minúscula.")
