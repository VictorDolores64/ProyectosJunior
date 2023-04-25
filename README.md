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
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()

# Muestra la información biográfica
print("Nombre completo:", nombre)
print("Edad:", edad, "años")
print("Carrera:", carrera)
print("Nacionalidad:", nacionalidad)
print("Fecha de nacimiento:", fechaN.strftime('%d/%m/%Y'))
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
```

---

7. Adivina el número 

```python
```

---

8. Es un palindromo

```python
```

---

9. Calcula la propina

```python
```

---

10. Cortador de correo electrónico

```python
```

---

11. Generadora de letras

```python
```

---