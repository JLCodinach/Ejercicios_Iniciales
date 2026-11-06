letra = input("Introduce un carácter: ")

if len(letra) != 1:
    print("Debes introducir un solo carácter.")
elif letra.isdigit():
    print("El valor introducido es un número.")
elif not letra.isalpha():
    print("El valor introducido es un símbolo")
elif letra.isupper():
    print("La letra es mayúscula")
elif letra.islower():
    print("La letra es minúscula")