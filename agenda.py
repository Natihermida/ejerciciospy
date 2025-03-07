class Contacto:
    """Clase para representar un contacto."""
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"


class Agenda:
    """Clase para gestionar la lista de contactos."""
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email):
        """Añade un nuevo contacto a la agenda."""
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print(f"\n✅ Contacto '{nombre}' agregado con éxito.")

    def buscar_contacto(self, nombre):
        """Busca un contacto por su nombre."""
        encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        if encontrados:
            print("\n🔎 Contacto encontrado:")
            for contacto in encontrados:
                print(contacto)
        else:
            print(f"\n❌ No se encontró ningún contacto con el nombre '{nombre}'.")

    def eliminar_contacto(self, nombre):
        """Elimina un contacto por su nombre."""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print(f"\n🗑 Contacto '{nombre}' eliminado con éxito.")
                return
        print(f"\n❌ No se encontró el contacto '{nombre}' para eliminar.")

    def mostrar_contactos(self):
        """Muestra todos los contactos guardados en la agenda."""
        if self.contactos:
            print("\n📖 Lista de contactos:")
            for contacto in self.contactos:
                print(contacto)
        else:
            print("\n⚠ No hay contactos en la agenda.")

def menu():
    """Función principal que muestra el menú y gestiona la agenda."""
    agenda = Agenda()

    while True:
        print("\n📌 Menú de Agenda:")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agenda.agregar_contacto(nombre, telefono, email)
        elif opcion == "2":
            nombre = input("Introduce el nombre a buscar: ")
            agenda.buscar_contacto(nombre)
        elif opcion == "3":
            nombre = input("Introduce el nombre a eliminar: ")
            agenda.eliminar_contacto(nombre)
        elif opcion == "4":
            agenda.mostrar_contactos()
        elif opcion == "5":
            print("\n👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\n⚠ Opción inválida, intenta de nuevo.")

# Ejecutar el programa
menu()

