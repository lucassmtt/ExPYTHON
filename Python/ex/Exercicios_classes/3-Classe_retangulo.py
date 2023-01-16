# Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

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
