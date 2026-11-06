#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice. 
#VERSION CON PALABRAS
text = "A quién madruga Dios ayuda"
print("A quién madruga Dios ayuda")

#VERSION CON INPUT
#text = input("Introduce una frase: ")
#print(text)

#VERSION CON PALABRAS
x1 = "Dios"
y1 = "dios"
z1 = "madruga"

#VERSION CON INPUT
#x1 = input("Escriva una palabra de la frase anterior:")
#y1 = input("Escriva una palabra de la frase anterior:")
#z1 = input("Escriva una palabra de la frase anterior:")

x2 = text.find(x1)
y2 = text.find(y1)
z2 = text.find(z1)

if x2 > 0:
    print(f"La palabra {x1} está en la frase y está en el índice {x2}")
else:
    print("La palabra no está en la frase")

if y2 > 0:
    print(f"La palabra {y1} está en la frase y está en el índice {y2}")
else:
    print(f"La palabra {y1} no está en la frase")

if z2 > 0:
    print(f"La palabra {z1} está en la frase y está en el índice {z2}")
else:
    print(f"La palabra {z1} no está en la frase")