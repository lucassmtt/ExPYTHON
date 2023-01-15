class Retangulo:
    def __init__(self, comprimento, largura) -> int:
        self.comprimento = comprimento
        self.largura = largura

    def mudar_lado(self, novo_com, nova_larg) -> int:
        self.comprimento = novo_com
        self.largura = nova_larg

    def retorna_valor_lados(self):
        print(self.comprimento, self.largura)

    def calc_area(self):
        area = self.largura * self.comprimento
        return area

    def calc_perimetro(self):
        perimetro = 2 * int(self.largura + self.comprimento)
        return perimetro

reta = Retangulo(12, 20)
area = reta.calc_area()
perimetro = reta.calc_perimetro()
print(f'Perimetro = {perimetro}, área = {area}')
