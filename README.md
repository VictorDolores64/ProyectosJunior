# Programas Junior Python

---
1. Par o Impar
```python
# Se solicita el numero
numero = int(input("Ingrese un número entero: "))

# Valida si el número es par o impar
if numero % 2 == 0:
    print(numero, "es un número par.")
else:
    print(numero, "es un número impar.")
```
---
2. Mab Libs
```python
# Variables
nombre = input("Ingrese tu nombre: ")
sustantivo = input("Ingrese un sustantivo: ")
verbo = input("Ingrese un verbo: ")
adjetivo = input("Ingrese un adjetivo: ")

# Se crea una historia con los datos ingresados
historia = f"{nombre} observó un {sustantivo} en la escuela y decidió {verbo} con él. Fue una experiencia {adjetivo} que nunca olvidará."

#Muestra la historia
print(historia)
```
---

3. El recuento de palabras

```python
# Se solicita el texto 
texto = input("Ingrese el texto que deseas contar: ")

# Se divide el texto por palabras
palabras = texto.split()

# Se cuenta el número de palabras
num_palabras = len(palabras)

# Muestra el número de palabras
print("El texto ingresado tiene", num_palabras, "palabras.")
```

---
4. Información biográfica

```python
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
```

---

5. ¿Cuál es mi acrónimo?  

```python
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


```

---

6. Piedra, papel y tijeras 

```python
#Importa la libreria de azar
import random

# Opciones a escoger por el jugador
opc = ["piedra", "papel", "tijeras"]

# Validación para la opción del usuario
def oU():
    eleccion = input("Elige piedra, papel o tijeras: ")
    while eleccion not in opc:
        eleccion = input("Elección no válida. Elige piedra, papel o tijeras: ")
    return eleccion

# Función para asignar opción de la computadora
def oC():
    return random.choice(opc)

# Función para determinar el resultado del juego
def ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif usuario == "piedra":
        if computadora == "papel":
            return "Gana la computadora"
        else:
            return "Ganas tú"
    elif usuario == "papel":
        if computadora == "tijeras":
            return "Gana la computadora"
        else:
            return "Ganas tú"
    elif usuario == "tijeras":
        if computadora == "piedra":
            return "Gana la computadora"
        else:
            return "Ganas tú"

# Juego principal
while True:
    # Obtener las elecciones
    usuario = oE()
    computadora = oC()

    # Mostrar las elecciones
    print("Tú elegiste:", usuario)
    print("La computadora eligió:", computadora)

    # Determinar el ganador
    resultado = ganador(usuario, computadora)

    # Mostrar el resultado
    print(resultado)
    jugar = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar != "s":
        break

```

---

7. Adivina el número 

```python
import random

def guess_number():
    # Generar un número aleatorio entre un rango de 1 y 100
    number = random.randint(1, 100)
    tries = 0
    
    while True:
        # Pedir al usuario que adivine el número
        guess = int(input("Adivina el número entre 1 y 100: "))
        tries += 1
        
        # Comprobar si el usuario adivinó el número
        if guess == number:
            print("¡Felicidades! Adivinaste el número en", tries, "intentos.")
            break
        elif guess < number:
            print("El número es más grande. Intenta de nuevo.")
        else:
            print("El número es más pequeño. Intenta de nuevo.")
            
guess_number()

```

---

8. Es un palindromo

```python
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

```

---

9. Calcula la propina

```python
# Pedir al usuario que ingrese el total de la cuenta y el porcentaje de propina
totalC = float(input("Ingresa el total de la cuenta: "))
porcentajeP = float(input("Ingresa el porcentaje de propina que deseas dejar (por ejemplo, 10 para el 10%): "))

# Calcular la propina y el total a pagar
propina = totalC * (porcentajeP / 100)
totalP = totalC+ propina

# Imprimir el monto de la propina y el total a pagar
print("La propina es:", propina)
print("El total a pagar es:", totalP)

```

---

10. Cortador de correo electrónico

```python
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

```

---

11. Generadora de letras

```python
import random

# Definir una lista de letras
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Pedir al usuario que ingrese el número de letras que desea generar
cantidadL = int(input("¿Cuántas letras deseas generar?: "))

# Generar las letras al azar y unirlas en una cadena
letrasG = ''.join(random.choices(letras, k=cantidad_L))

# Imprimir las letras generadas
print("Las letras generadas son:", letrasG)

```

---