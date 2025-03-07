# Función para convertir kilómetros a millas
def km_a_millas(km):
    # Se multiplica el valor en kilómetros por 0.621371 para obtener el equivalente en millas
    return km * 0.621371

# Función para convertir grados Celsius a Fahrenheit
def celsius_a_fahrenheit(c):
    # La fórmula para convertir Celsius a Fahrenheit es (C * 9/5) + 32
    return (c * 9/5) + 32

# Función para convertir gramos a libras
def gramos_a_libras(g):
    # Se multiplica el valor en gramos por 0.00220462 para obtener el equivalente en libras
    return g * 0.00220462

# Función para convertir metros a pulgadas
def metros_a_pulgadas(m):
    # Se multiplica el valor en metros por 39.3701 para obtener el equivalente en pulgadas
    return m * 39.3701

# Función para convertir litros a galones
def litros_a_galones(l):
    # Se multiplica el valor en litros por 0.264172 para obtener el equivalente en galones
    return l * 0.264172

# Menú de opciones para que el usuario seleccione qué conversión desea hacer
print("Seleccione la conversión que desea realizar:")
print("1. Kilómetros a Millas")
print("2. Celsius a Fahrenheit")
print("3. Gramos a Libras")
print("4. Metros a Pulgadas")
print("5. Litros a Galones")

# Se solicita al usuario que ingrese la opción deseada
opcion = int(input("Ingrese el número de la conversión deseada: "))

# Dependiendo de la opción seleccionada, se realiza la conversión correspondiente
if opcion == 1:
    # Si se elige la opción 1 (Kilómetros a Millas)
    valor = float(input("Ingrese la cantidad en kilómetros: "))  # Solicita el valor en kilómetros
    # Realiza la conversión y muestra el resultado con dos decimales
    print(f"{valor} km equivale a {km_a_millas(valor):.2f} millas.")
elif opcion == 2:
    # Si se elige la opción 2 (Celsius a Fahrenheit)
    valor = float(input("Ingrese la temperatura en Celsius: "))  # Solicita el valor en Celsius
    # Realiza la conversión y muestra el resultado con dos decimales
    print(f"{valor}°C equivale a {celsius_a_fahrenheit(valor):.2f}°F.")
elif opcion == 3:
    # Si se elige la opción 3 (Gramos a Libras)
    valor = float(input("Ingrese la cantidad en gramos: "))  # Solicita el valor en gramos
    # Realiza la conversión y muestra el resultado con cuatro decimales
    print(f"{valor} g equivale a {gramos_a_libras(valor):.4f} libras.")
elif opcion == 4:
    # Si se elige la opción 4 (Metros a Pulgadas)
    valor = float(input("Ingrese la cantidad en metros: "))  # Solicita el valor en metros
    # Realiza la conversión y muestra el resultado con dos decimales
    print(f"{valor} m equivale a {metros_a_pulgadas(valor):.2f} pulgadas.")
elif opcion == 5:
    # Si se elige la opción 5 (Litros a Galones)
    valor = float(input("Ingrese la cantidad en litros: "))  # Solicita el valor en litros
    # Realiza la conversión y muestra el resultado con dos decimales
    print(f"{valor} L equivale a {litros_a_galones(valor):.2f} galones.")
else:
    # Si el usuario ingresa una opción no válida
    print("Opción no válida. Por favor, seleccione un número del 1 al 5.")


