import random

# Definir una lista de letras
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Pedir al usuario que ingrese el número de letras que desea generar
cantidadL = int(input("¿Cuántas letras deseas generar?: "))

# Generar las letras al azar y unirlas en una cadena
letrasG = ''.join(random.choices(letras, k=cantidadL))

# Imprimir las letras generadas
print("Las letras generadas son:", letrasG)