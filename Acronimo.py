# Se solicita una frase
frase = input("Ingrese la frase para generar el acrónimo: ")

# Se divide la frase por palabras
palabras = frase.split()

# Se hace un ciclo de la primera letra de cada palabra
acronimo = ""
for palabra in palabras:
    acronimo += palabra[0].upper()

# Se muetra el acrónimo 
print("El acrónimo correspondiente a la frase ingresada es:", acronimo)
