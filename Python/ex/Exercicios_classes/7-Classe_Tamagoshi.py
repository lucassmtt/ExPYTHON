# Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade;
# Retornar Nome, Fome, Saúde e Idade Obs:
# Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
# este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
# então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

class Bichicho_eletronico:
    def __init__(self, nome=' ', fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = None

    def mudar_nome(self, novo_nome):
        self.nome = novo_nome
        print(self.nome)

    def mudar_fome(self, fome):
        self.fome = fome
        print(f'Fome == {self.fome}')
        self.calc_humor()

    def mudar_saude(self, nova_saude):
        self.saude = nova_saude
        print(f'Saúde == {self.saude}')
        self.calc_humor()

    def mudar_idade(self, nova_idade):
        self.idade = nova_idade
        print(self.idade)

    def calc_humor(self):
        if self.saude <= 50 and self.fome >= 50:
            self.humor = 'Bravo'
            return print(f'O seu bichicho está {self.humor}')

        else:
            self.humor = 'Normal'
            return print(f'O seu bichicho está {self.humor}')


bichicho1 = Bichicho_eletronico('Tamagoshi', 30, 100, 44)
bichicho1.mudar_saude(10)
bichicho1.mudar_fome(100)
