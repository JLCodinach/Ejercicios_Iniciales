import math
#Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos  resultados de todo el proceso (raíz y división). 
numero = float(input("Introduce un número: "))
raiz_cuadrada = math.sqrt(numero)
division = raiz_cuadrada / 2
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")
print(f"El resultado de dividir la raíz cuadrada entre 2 es: {division}")
