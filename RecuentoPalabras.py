# Se solicita el texto 
texto = input("Ingrese el texto que deseas contar: ")

# Se divide el texto por palabras
palabras = texto.split()

# Se cuenta el número de palabras
num_palabras = len(palabras)

# Muestra el número de palabras
print("El texto ingresado tiene", num_palabras, "palabras.")