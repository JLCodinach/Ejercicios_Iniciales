#Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif
frase = input("Introduce una frase: ")

num_frase = len(frase)

if num_frase > 11:
    print("La frase tiene más de 11 caracteres.")
elif num_frase == 11:
    print("La frase tiene 11 caracteres.")
else:
    print("La frase tiene menos de 11 caracteres.")