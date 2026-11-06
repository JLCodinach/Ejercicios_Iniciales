#Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas 
#VERSION CON INPUT
#text = input("Introduce una frase: ")
#print(text)

#VERSION CON PALABRAS
text = "A quién madruga Dios ayuda"
print("A quién madruga Dios ayuda")

#VERSION CON INPUT
#x1 = input("Escriva una palabra de la frase anterior:")
#y1 = input("Escriva una palabra de la frase anterior:")
#z1 = input("Escriva una palabra de la frase anterior:")

#VERSION CON PALABRAS
x1 = "Dios"
y1 = "dios"
z1 = "madruga"

x2 = text.find(x1)
y2 = text.find(y1)
z2 = text.find(z1)

if x2 >= 0:
    print(f"La palabra {x1} está en la frase y está en el índice {x2}")
else:
    text = text.lower()
    x1 = x1.lower()
    x2 = text.find(x1)

    if x2 >= 0:
        print(f"La palabra -{x1}- está en la frase y está en el índice {x2}")
    else:
        print(f"La palabra -{x1}- no está en la frase")

if y2 >= 0:
    print(f"La palabra -{y1}- está en la frase y está en el índice {y2}")
else:
    text = text.lower()
    y1 = y1.lower()
    y2 = text.find(y1)
    if y2 >= 0:
        print(f"La palabra -{y1}- está en la frase y está en el índice {y2}")
    else:
        print(f"La palabra -{y1}- no está en la frase")

if z2 >= 0:
    print(f"La palabra -{z1}- está en la frase y está en el índice {z2}")
else:
    text = text.lower()
    z1 = z1.lower()
    z2 = text.find(z1)
    if z2 >= 0:
        print(f"La palabra -{z1}- está en la frase y está en el índice -{z2}-")
    else:
        print(f"La palabra -{z1}- no está en la frase")

