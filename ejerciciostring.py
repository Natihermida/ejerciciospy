def contar_palabras(texto):
    """Cuenta la cantidad de palabras en el texto."""
    return len(texto.split())

def contar_vocales_consonantes(texto):
    """Cuenta la cantidad de vocales y consonantes en el texto."""
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    num_vocales = sum(1 for letra in texto if letra in vocales)
    num_consonantes = sum(1 for letra in texto if letra in consonantes)
    
    return num_vocales, num_consonantes

def palabra_mas_larga(texto):
    """Encuentra la palabra más larga en el texto."""
    palabras = texto.split()
    if palabras:
        return max(palabras, key=len)
    return ""

# Solicitar entrada al usuario
texto = input("Introduce un texto: ")

# Procesar el texto
num_palabras = contar_palabras(texto)
num_vocales, num_consonantes = contar_vocales_consonantes(texto)
palabra_larga = palabra_mas_larga(texto)

# Mostrar resultados
print("\nResultados:")
print("Cantidad de palabras:", num_palabras)
print("Cantidad de vocales:", num_vocales)
print("Cantidad de consonantes:", num_consonantes)
print("La palabra más larga:", palabra_larga)

