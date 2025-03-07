import random

# Lista de palabras para el juego
PALABRAS = ["python", "programacion", "ahorcado", "desarrollo", "inteligencia"]

# Dibujos del ahorcado según los intentos restantes
AHORCADO_DIBUJO = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """  # Estado inicial (sin fallos)
]


def elegir_palabra():
    """Selecciona una palabra al azar de la lista."""
    return random.choice(PALABRAS)


def mostrar_progreso(palabra, letras_adivinadas):
    """Muestra la palabra con las letras adivinadas y guiones para las desconocidas."""
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra)


def jugar_ahorcado():
    """Función principal del juego del ahorcado."""
    palabra_secreta = elegir_palabra()
    letras_adivinadas = set()
    intentos_restantes = 6  # Intentos máximos

    print("¡Bienvenido al juego del Ahorcado!")

    while intentos_restantes > 0:
        print(AHORCADO_DIBUJO[intentos_restantes])  # Muestra el dibujo según los intentos restantes
        print("\nPalabra:", mostrar_progreso(palabra_secreta, letras_adivinadas))
        print(f"Intentos restantes: {intentos_restantes}")

        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya intentaste con esa letra. Intenta con otra.")
            continue

        letras_adivinadas.add(letra)

        if letra in palabra_secreta:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Incorrecto. Pierdes un intento.")
            intentos_restantes -= 1

        if set(palabra_secreta).issubset(letras_adivinadas):
            print(AHORCADO_DIBUJO[intentos_restantes])  # Muestra la imagen final si gana antes
            print(f"\n¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
            break
    else:
        print(AHORCADO_DIBUJO[0])  # Muestra el ahorcado final
        print(f"\n¡Perdiste! La palabra era: {palabra_secreta}")

# Ejecutar el juego
jugar_ahorcado()

