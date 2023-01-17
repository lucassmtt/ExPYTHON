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

    def qtd_de_comida(self, comida_max):
        if (comida_max >= 0) and (comida_max <= 100):
            self.fome -= (self.fome * (comida_max / 100))

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.saude -= (self.saude * (quantidade / 100))


Woody = Bichicho_eletronico(nome='Woddy',fome=100, saude=50, idade=1)
Woody.calc_humor()
