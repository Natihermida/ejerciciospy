#Escribe un programa que solicite un número n y genere una lista con los primeros n números primos.
def es_primo(num):
    """Función que verifica si un número es primo."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeros_n_primos(n):
    """Función que genera una lista con los primeros n números primos."""
    primos = []
    num = 2  # Empezamos desde el primer número primo
    while len(primos) < n:
        if es_primo(num):
            primos.append(num)
        num += 1
    return primos

# Solicitar entrada del usuario
n = int(input("Ingrese la cantidad de números primos que desea obtener: "))
print("Los primeros", n, "números primos son:", primeros_n_primos(n))

