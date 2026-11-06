#Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo 
import math
a=float(input("Introduce el coeficiente a: "))
b=float(input("Introduce el coeficiente b: "))
c=float(input("Introduce el coeficiente c: "))

discriminante=b**2-4*a*c

if discriminante < 0:
    print("El valor de la raíz cuadrada es negativo.")
else:
    if a == 0:
        print(f"Error al dividir entre zero")
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Las soluciones son: x1 = {x1} y x2 = {x2}")