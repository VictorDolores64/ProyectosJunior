import re

# Pedir al usuario que ingrese su correo electrónico
email = input("Ingresa tu correo electrónico: ")

# Definir la expresión regular para el correo electrónico
patron = re.compile(r'([\w.-]+)@([\w.-]+)')

# Buscar el usuario y el dominio en el correo electrónico utilizando la expresión regular
match = patron.search(email)

# Imprimir el usuario y el dominio del correo electrónico
if match:
    usuario = match.group(1)
    dominio = match.group(2)
    print("Usuario:", usuario)
    print("Dominio:", dominio)
else:
    print("El correo electrónico no es válido.")