class Candidato:
    """Representa un candidato en la votación."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.votos = 0  # Inicializa con 0 votos

    def recibir_voto(self):
        """Incrementa en 1 el número de votos recibidos."""
        self.votos += 1


class Votante:
    """Representa a un votante registrado."""
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.ha_votado = False  # Inicialmente, no ha votado


class SistemaVotacion:
    """Gestiona el sistema de votación."""
    def __init__(self):
        self.candidatos = {}  # Diccionario con los candidatos
        self.votantes = {}  # Diccionario con los votantes registrados

    def registrar_candidato(self, nombre):
        """Registra un nuevo candidato."""
        if nombre in self.candidatos:
            print("\n⚠ El candidato ya está registrado.")
        else:
            self.candidatos[nombre] = Candidato(nombre)
            print(f"\n✅ Candidato '{nombre}' registrado con éxito.")

    def registrar_votante(self, nombre, dni):
        """Registra un nuevo votante con su DNI."""
        if dni in self.votantes:
            print("\n⚠ Este votante ya está registrado.")
        else:
            self.votantes[dni] = Votante(nombre, dni)
            print(f"\n✅ Votante '{nombre}' con DNI '{dni}' registrado con éxito.")

    def emitir_voto(self, dni, candidato):
        """Permite a un votante emitir su voto."""
        if dni not in self.votantes:
            print("\n❌ Votante no registrado.")
            return
        if self.votantes[dni].ha_votado:
            print("\n⚠ Ya has votado y no puedes volver a hacerlo.")
            return
        if candidato not in self.candidatos:
            print("\n❌ Candidato no válido.")
            return

        self.candidatos[candidato].recibir_voto()
        self.votantes[dni].ha_votado = True
        print(f"\n🗳 Voto registrado para '{candidato}'.")

    def mostrar_resultados(self):
        """Muestra los resultados de la votación."""
        if not self.candidatos:
            print("\n⚠ No hay candidatos registrados.")
            return

        print("\n📊 Resultados de la votación:")
        for nombre, candidato in self.candidatos.items():
            print(f"🗳 {nombre}: {candidato.votos} votos")
        ganador = max(self.candidatos.values(), key=lambda c: c.votos)
        print(f"\n🏆 Ganador: {ganador.nombre} con {ganador.votos} votos")


def menu():
    """Menú principal del sistema de votación."""
    sistema = SistemaVotacion()

    while True:
        print("\n📌 Menú de Votación:")
        print("1. Registrar candidato")
        print("2. Registrar votante")
        print("3. Emitir voto")
        print("4. Mostrar resultados")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del candidato: ")
            sistema.registrar_candidato(nombre)
        elif opcion == "2":
            nombre = input("Nombre del votante: ")
            dni = input("DNI del votante: ")
            sistema.registrar_votante(nombre, dni)
        elif opcion == "3":
            dni = input("Introduce tu DNI para votar: ")
            print("\nCandidatos disponibles:")
            for candidato in sistema.candidatos:
                print(f"🔹 {candidato}")
            candidato = input("Introduce el nombre del candidato a votar: ")
            sistema.emitir_voto(dni, candidato)
        elif opcion == "4":
            sistema.mostrar_resultados()
        elif opcion == "5":
            print("\n👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\n⚠ Opción inválida, intenta de nuevo.")

# Ejecutar el programa
menu()

