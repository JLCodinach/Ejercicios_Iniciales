#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado=float(input("Introduce el valor del lado del trapecio: "))
base_menor=float(input("Introduce el valor de la base menor del trapecio: "))
base_mayor=float(input("Introduce el valor de la base mayor del trapecio: "))
altura=float(input("Introduce el valor de la altura del trapecio: "))
area=(base_menor+base_mayor)*altura/2
perimetro=lado*2+base_menor+base_mayor
print(f"El área del trapecio es: {area}")
print(f"El perímetro del trapecio es: {perimetro}")