class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        """Inicializa una cuenta bancaria con un titular y saldo opcional."""
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        """Deposita dinero en la cuenta."""
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de {monto:.2f} realizado. Nuevo saldo: {self.saldo:.2f}")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    def retirar(self, monto):
        """Retira dinero de la cuenta si hay suficiente saldo."""
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto:.2f} realizado. Nuevo saldo: {self.saldo:.2f}")
        elif monto > self.saldo:
            print("Fondos insuficientes.")
        else:
            print("El monto a retirar debe ser mayor a 0.")

    def consultar_saldo(self):
        """Consulta el saldo actual de la cuenta."""
        print(f"Saldo actual de {self.titular}: {self.saldo:.2f}")

    def transferir(self, otra_cuenta, monto):
        """Transfiere dinero a otra cuenta bancaria."""
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            otra_cuenta.saldo += monto
            print(f"Transferencia de {monto:.2f} a {otra_cuenta.titular} realizada con éxito.")
        elif monto > self.saldo:
            print("Fondos insuficientes para la transferencia.")
        else:
            print("El monto a transferir debe ser mayor a 0.")

# Prueba del código
cuenta1 = CuentaBancaria("Juan", 1000)
cuenta2 = CuentaBancaria("María", 500)

cuenta1.consultar_saldo()
cuenta2.consultar_saldo()

cuenta1.depositar(200)
cuenta1.retirar(500)

cuenta1.transferir(cuenta2, 300)
cuenta1.consultar_saldo()
cuenta2.consultar_saldo()

