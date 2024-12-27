class SaldoError(ValueError):
    def __init__(self, message="Saldo no puede ser menor a 0"):
        self.message = message
        super().__init__(self.message)


class ClienteError(ValueError):
    def __init__(self, cliente):
        self.message = f'Cliente "{cliente}" no encontrado'
        super().__init__(self.message)


class Cliente:
    def __init__(self, nombre: str, saldo: int):
        self.nombre = nombre
        if saldo < 0:
            raise SaldoError()
        self.saldo = saldo

    def retirar(self, cantidad: int):
        if cantidad > self.saldo:
            raise ValueError("No se tiene saldo suficiente")
        self.saldo -= cantidad

    def depositar(self, cantidad):
        self.saldo += cantidad

    def __str__(self):
        return f"Cliente: {self.nombre}, Saldo: {self.saldo}"


class Cajero:
    total = 0

    def __init__(self, *argv: Cliente):
        for cliente in argv:
            self.total += cliente.saldo
        self.clientes = argv

    def operar(self, nombre_cliente, cantidad: int):
        cliente = self.__get_cliente(nombre_cliente)
        if cliente is None:
            raise ClienteError(nombre_cliente)
        if cantidad < 0:
            cliente.retirar(cantidad * -1)
        else:
            cliente.depositar(cantidad)

    def deposito_total(self):
        return sum(cliente.saldo for cliente in self.clientes)

    def __get_cliente(self, nombre_cliente):
        return next(
            (cliente for cliente in self.clientes if cliente.nombre == nombre_cliente),
            None,
        )

    def __str__(self):
        return "\n".join(str(cliente) for cliente in self.clientes)


if __name__ == "__main__":
    ricardo = Cliente("Ricardo", 100)
    panchito = Cliente("Panchito", 50)
    filomeno = Cliente("Filomeno", 500)
    cajero = Cajero(ricardo, panchito, filomeno)
    assert cajero.deposito_total() == 650
    assert cajero.total == 650
    cajero.operar("Ricardo", -50)
    assert ricardo.saldo == 50
    cajero.operar("Panchito", 50)
    assert panchito.saldo == 100
    cajero.operar("Filomeno", -400)
    assert filomeno.saldo == 100
    assert cajero.deposito_total() == 250
    print(cajero)
