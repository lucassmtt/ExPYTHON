from abc import abstractmethod, abstractclassmethod


class Conta:
    def __init__(self, numero_agencia, numero_conta, saldo=0):
        self._agencia = numero_agencia
        self._conta = numero_conta
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor):
        self._saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    def detalhes(self, msg):
        print(f'O seu saldo atual é de {self._saldo:.2f} {msg}')
        print('-'*30)


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self._saldo - valor

        if valor_pos_saque >= 0:
            self._saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self._saldo

        print('Não foi possível sacar o valor desejado...')
        self.detalhes(f'(Saque NEGADO {valor}, )')


class ContaCorrente(Conta):
    def __init__(self, numero_agencia, numero_conta, saldo=0, limite=0):
        super().__init__(numero_agencia, numero_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self._saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self._saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self._saldo

        print(f'Não foi possível sacar o valor desejado...')
        print(f'Seu limite é {self.limite}')
        self.detalhes(f'(SAQUE NEGADO) {valor}')


# if __name__ == '__main__':
    # conta_p_01 = ContaPoupanca(10242, 1834729)
    # conta_p_01.sacar(1)
    # conta_p_01.depositar(80)
    # conta_p_01.sacar(85)
    # print('-'*30)
    # conta_c_01 = ContaCorrente(10242, 1834729, 0, 100)
    # print('-'*20)
    # conta_c_01.sacar(1)
    # conta_c_01.depositar(1)
    # conta_c_01.sacar(1)
    # conta_c_01.sacar(1)
    # conta_c_01.sacar(1)
