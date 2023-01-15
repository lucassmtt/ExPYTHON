class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def Troca_cor(self, nova_cor):
        self.cor = nova_cor

    def Mostra_cor(self):
        print(self.cor)


bola1 = Bola('Azul', '13cm', 'Borracha')
