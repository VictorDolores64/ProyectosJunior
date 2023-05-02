#Importamos el formato de fecha
import datetime

# Solicitamos los datos al usuario
nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
carrera = input("Ingrese su profesión: ")
nacionalidad = input("Ingrese su nacionalidad: ")
fechaN = input("Ingrese su fecha de nacimiento (formato: AAAA-MM-DD): ")

# Los caracteres ingresados se convierten en fecha
fecha_nacimiento = datetime.datetime.strptime(fechaN, '%Y-%m-%d').date()

# Muestra la información biográfica
print("Nombre completo:", nombre)
print("Edad:", edad, "años")
print("Carrera:", carrera)
print("Nacionalidad:", nacionalidad)
print("Fecha de nacimiento:", fecha_nacimiento.strftime('%d/%m/%Y'))