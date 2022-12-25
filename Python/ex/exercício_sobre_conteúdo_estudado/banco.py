import contas
import pessoas


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None,
    ):

        self.agencias = agencias or []
        self.cliente = clientes or []
        self.contas = contas or []


    def __repr__(self):
        class_name = __class__.__name__
        attr = f'({self.agencias!r}, {self.cliente!r}, {self.contas!r})'
        return f'{class_name}, {attr}'


    def _checa_agencia(self, conta):
        if conta._agencia in self.agencias:
            return True
        return False


    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False


    def _checa_cliente(self, cliente):
        if cliente in self.cliente:
            return True
        return False


    def _checa_se_a_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False


    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) \
               and self._checa_conta(conta)\
               and self._checa_cliente(cliente)\
               and self._checa_se_a_conta_e_do_cliente(cliente, conta)

if __name__ == '__main__':
    ############ criando clientes
    ############
    cliente_01 = pessoas.Cliente('Lucas Motta', 19)
    cliente_02 = pessoas.Cliente('Maria Betânia', 66)
    ########### criando a conta do cliente
    ###########
    conta_do_cliente_01 = contas.ContaCorrente(11, 13, 0, 0)
    conta_do_cliente_02 = contas.ContaPoupanca(12, 14, 100)
    ##atribuindo a variável conta do cliente a sua conta no banco
    #########
    cliente_01.conta = conta_do_cliente_01
    cliente_02.conta = conta_do_cliente_02
    ###############################
    ### criando e adicionando clientes ao banco
    bradesco = Banco()
    bradesco.cliente.extend([cliente_01, cliente_02])
    #############################
    ##adicionando as contas dos clientes ao banco
    bradesco.contas.extend([conta_do_cliente_01, conta_do_cliente_02])
    ##adicionar as agencias
    bradesco.agencias.extend([11, 12])

    #print(bradesco.autenticar(cliente_01, conta_do_cliente_01))
    if bradesco.autenticar(cliente_01, conta_do_cliente_01):
        conta_do_cliente_01.depositar(100)
        print(cliente_01.conta)
