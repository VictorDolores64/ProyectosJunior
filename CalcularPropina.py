# Pedir al usuario que ingrese el total de la cuenta y el porcentaje de propina
totalC = float(input("Ingresa el total de la cuenta: "))
porcentajeP = float(input("Ingresa el porcentaje de propina que deseas dejar (por ejemplo, 10 para el 10%): "))

# Calcular la propina y el total a pagar
propina = totalC * (porcentajeP / 100)
totalP = totalC+ propina

# Imprimir el monto de la propina y el total a pagar
print("La propina es:", propina)
print("El total a pagar es:", totalP)
