# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago)
# e pelo menos os métodos comer(), verBucho() e digerir().
# Faça um programa ou teste interativamente, criando pelo menos dois macacos,
# alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
# Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.estomago = []

    def comer(self, *alimentos):
        for alimento in alimentos:
            print(f'O {self.nome} comeu {alimento}')
            self.estomago.append(alimento)

    def mostrar_estomago(self):
        for alimento in self.estomago:
            print(f'No estômago do {self.nome}, tem {alimento}.')

    def digerir_comida(self):
        self.estomago.clear()
        print(f'O estômago do macaco {self.nome} está vazio.')


gorila = Macaco('Gorila Koko')
gorila.comer('Arroz', 'feijão')
gorila.mostrar_estomago()
gorila.digerir_comida()

chimpanze = Macaco('Tiao')
chimpanze.comer(gorila.nome)
