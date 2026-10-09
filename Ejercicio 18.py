#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine. 

num_menores = int(input("Introduce el número de menores: "))
num_adultos = int(input("Introduce el número de adultos: "))

total_menores = num_menores * 12 * 0.5
total_adultos = num_adultos * 12 * 0.9

print(f"El total a pagar es: {total_menores + total_adultos} €")