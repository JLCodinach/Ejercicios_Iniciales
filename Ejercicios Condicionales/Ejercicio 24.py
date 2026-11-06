#Corrige los errores del siguiente código y comprueba que se ejecuta correctamente
var_peso=float(input("Introduce el peso: ")) 
var_altura=float(input("Introduce la altura: ")) 
var_imc=var_peso / var_altura**2 
print(f"Si pesas {var_peso} kilos y mides {var_altura}, tu IMC es: {var_imc}") 
if var_imc>25: 
    print("Hay sobrepeso") 
else: 
    print("Estás dentro de los parámetros normales")