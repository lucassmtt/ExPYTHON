class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: int):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, tempo_de_envelhecimento: int):
        self.tempo_envelhecimento = tempo_de_envelhecimento
        self.idade += self.tempo_envelhecimento
        if self.idade <= 21:
            altura_crescida_nesse_tempo = 0.5 * tempo_de_envelhecimento
            self.altura += altura_crescida_nesse_tempo

    def engordar(self, peso_engordar: float):
        self.peso += peso_engordar

    def emagrecer(self, peso_emagrecer: float):
        self.peso -= peso_emagrecer

    def crescer(self, altura_cresc):
        self.altura += altura_cresc

pessoa_01 = Pessoa('Gabriel', 15, 1.93, 180)
pessoa_01.envelhecer(5)
print(pessoa_01.altura)