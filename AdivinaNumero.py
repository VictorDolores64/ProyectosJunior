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