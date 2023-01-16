# Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área

class Quadrado:
    def __init__(self, tam_lado):
        self.tamanho = tam_lado

    def Mudar_valor_lado(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def retorno_valor_lado(self):
        print(self.tamanho)

    def calc_area(self):
        res = self.tamanho ** 2
        return res


q1 = Quadrado(12)
area = q1.calc_area()
print(area)