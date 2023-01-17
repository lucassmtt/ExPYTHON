#classe ponto e retangulo

class Ponto:
    def __init__(self, ponto_x, ponto_y):
        self.ponto_x = ponto_x
        self.ponto_y = ponto_y

    def print_ponto(self):
        self.cartesiano = (self.ponto_x, self.ponto_y)
        print(self.cartesiano)
class Retangulo(Ponto):
    def loc_centro(self):
        height_p_2 = int(self.ponto_x) / 2
        width_p_2 = int(self.ponto_y) / 2
        return Ponto(height_p_2, width_p_2)

cartesiano_1 = Retangulo(1, 4)
cartesiano_1.print_ponto()

novo_ponto = cartesiano_1.loc_centro()
novo_retangulo = Retangulo(novo_ponto.ponto_x, novo_ponto.ponto_y)
novo_retangulo.print_ponto()
