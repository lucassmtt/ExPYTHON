class Carro:
    def __init__(self, nome, modelo):
        self.nome = nome
        self.modelo = modelo
        self.velocidade = 1

    def acelerar(self):
        self.velocidade = Motor()


class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.valocidade = None

    def multiplica_velocidade(self):
        self.multiplicador = None

    @multiplica_velocidade.setter
    def multiplica_velocidade(self, valor):
        self.velocidade = 1
        return self.velocidade * valor

