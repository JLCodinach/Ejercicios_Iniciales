import math
#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
diametro=float(input("Introduce el diámetro del círculo: "))
radio=diametro/2
area=math.pi*radio**2
perimetro=2*math.pi*radio
print(f"Área: {area:.1f}")
print(f"Perímetro: {perimetro:.1f}")