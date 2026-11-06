#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota = float(input("Introduce tu nota: "))

if nota<0 or nota>10:
    print("Nota no válida. Debe estar entre 0 y 10.")
elif nota>=8.5:
    print("Excelente.")
elif nota>=6.5:
    print("Notable.")
elif nota>=5:
    print("Satisfactorio.")
else:
    print("Insuficiente.")