class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        #.__class__.__name
        #  type(self)
        nome_classe = self.__class__.__name__
        return f'{nome_classe} (x={self.x}, y={self.y})'

    def __add__(self, other):
        novo_valor_x = self.x + other.x
        novo_valor_y = self.y + other.y
        return Ponto(novo_valor_x, novo_valor_y)

    def __lt__(self, other):
        valor_self = self.x + self.y
        valor_other = other.x + other.y
        if valor_self > valor_other:
            print(f'Valor self é maior ({valor_self}) > ({valor_other})')
            return valor_self
        else:
            print(f'Valor other é maior ({valor_other}) > ({valor_self})')
            return valor_other


ponto_1 = Ponto(1, 5)
ponto_2 = Ponto(3, 5)
#
# ponto_3 = ponto_1 + ponto_2
# print(ponto_3.__repr__())
maior = (ponto_1 > ponto_2)
print(maior)