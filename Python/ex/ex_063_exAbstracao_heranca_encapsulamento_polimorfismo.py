class Conta:
    def __init__(self, numero_agencia, numero_conta, saldo):
        self._agencia = numero_agencia
        self._conta = numero_conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._num_agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo


class ContaCorrente(Conta):
    ...


class ContaPoupanca(Conta):
    ...


class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def idade(self):
        return self._idade
class Cliente(Pessoa):
    ...

lucas = Cliente('Lucas', 'Motta', 18)
print(lucas.nome)
print(lucas.sobrenome)
print(lucas.idade)