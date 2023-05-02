def palindromo(texto):
    # Convierte el texto en minusculas y elimina los espacios
    texto = texto.lower().replace(" ", "")
    # Verificar si el texto es igual al texto invertido
    return texto == texto[::-1]

# Pedir al usuario que ingrese un texto para verificar si es un palíndromo
textoU = input("Ingresa un texto para verificar si es un palíndromo: ")

# Verificar si el texto es un palíndromo e imprimir el resultado
if palindromo(textoU):
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palíndromo.")