from datetime import date

class Pessoa:
    ANO_ATUAL = date.today().year
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):

        return Pessoa.ANO_ATUAL - self.idade

pessoa_01 = Pessoa('Guilherme', 18)
pessoa_02 = Pessoa('João', 24)

# print(pessoa_01.get_ano_nascimento())
# print(pessoa_02.get_ano_nascimento())
# print(Pessoa.ANO_ATUAL)

print(vars(pessoa_01))

pessoa_01.__dict__['nome'] = 'José'

print(vars(pessoa_01))