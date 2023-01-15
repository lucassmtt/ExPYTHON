class ContaCorrente:
    def __init__(self, numero_conta, nome_do_dono, saldo):
        self.conta = numero_conta
        self.nome = nome_do_dono
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        print(self.saldo)


cliente01 = ContaCorrente(999, 'João', 100)
cliente01.sacar(10)
cliente01.mostrar_saldo()
cliente01.depositar(30)
cliente01.mostrar_saldo()