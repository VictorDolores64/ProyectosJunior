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
    usuario = oU()
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
