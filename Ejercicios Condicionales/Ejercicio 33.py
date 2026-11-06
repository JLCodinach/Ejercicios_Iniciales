#rograma un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años 

#VERSIÓN INPUT
#frase = input("Introduce una frase")

frase = "No hay mal que dure cien años"
vocales = "aáàeéèiíìoóòuúù"  #Por si esta en catalán pongo tildes abiertas
contador = 0

for letra in frase.lower():
    if letra in vocales:
        contador += 1

print(f"La frase tiene {contador} vocales.")