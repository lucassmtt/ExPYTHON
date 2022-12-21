class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def add_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print(f'Apagando {self.rua, self.numero}')

cliente_01 = Cliente('Lucas Motta')
cliente_01.add_endereco('Rua Jacobi', 232)

