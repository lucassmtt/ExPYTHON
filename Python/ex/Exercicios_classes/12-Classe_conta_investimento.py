class Conta:
    def __init__(self, numero_conta=0, nome='', saldo=0):
        self.numero = numero_conta
        self.nome = nome
        self.saldo = saldo

    def setNome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

class contaInvestimento(Conta):
    def __init__(self, numero, nome, saldo, taxaJuros):
        super().__init__(numero, nome, saldo)
        self.taxa_juros = taxaJuros

    def add_juros(self):
        self.saldo += (self.saldo * self.taxa_juros / 100)


poupanca = contaInvestimento(12221, 'Lucas', 1340, 10)
print(vars(poupanca))
poupanca.add_juros()
poupanca.add_juros()
poupanca.add_juros()
poupanca.add_juros()
poupanca.add_juros()
print(vars(poupanca))