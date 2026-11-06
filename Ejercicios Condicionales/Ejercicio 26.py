#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.letra = input("Introduce una letra: ")
letra = input("Introduce una letra: ")

if len(letra) != 1 or letra.isalpha()==False:
    print("La  letra es mayuscula ¿?")
else:
    if letra.isupper()==True:
        print("La letra es mayuscula")
    elif letra.islower()==True:
        print("La letra es minuscula")

    
