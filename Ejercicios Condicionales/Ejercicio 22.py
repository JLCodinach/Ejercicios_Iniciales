#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.  
nota=float(input("Introduce tu nota: "))
if nota<5:
    print("Has suspendido.")
else:
    print("Has aprobado.")
