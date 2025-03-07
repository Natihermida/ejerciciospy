def cifrado_cesar(texto, desplazamiento):
    """Cifra un texto usando el Cifrado César con el desplazamiento dado."""
    resultado = ""
    
    for caracter in texto:
        if caracter.isalpha():  # Verifica si es una letra
            ascii_base = ord('A') if caracter.isupper() else ord('a')
            nuevo_caracter = chr((ord(caracter) - ascii_base + desplazamiento) % 26 + ascii_base)
            resultado += nuevo_caracter
        else:
            resultado += caracter  # No modifica caracteres especiales ni espacios

    return resultado

# Solicitar entrada del usuario
texto = input("Introduce el texto a cifrar: ")
desplazamiento = int(input("Introduce la clave de desplazamiento (número entero): "))

# Obtener el texto cifrado
texto_cifrado = cifrado_cesar(texto, desplazamiento)

# Mostrar el resultado
print("\nTexto cifrado:", texto_cifrado)

