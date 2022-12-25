import contas


class Pessoa:
    def __init__(self, nome: str, idade:int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self:str):
        return self._nome

    @nome.setter
    def nome(self, nome:str):
        self._nome = nome

    @property
    def idade(self:int):
        return self._idade

    @idade.setter
    def idade(self, idade:int):
        self._idade = idade

    def __repr__(self):
        class_name = f'{self.__class__.__name__}'
        name_idade = f'{self.nome!r}, {self._idade!r}'
        return f'{class_name}({name_idade})'

class Cliente(Pessoa):
    def __init__(self, nome: str, idade:int) -> None:
        super().__init__(nome, idade)
        self.conta = contas.ContaCorrente | None

if __name__ == '__main__':

    c1 = Cliente('Lucas', 19)
    c1.conta = contas.ContaCorrente(221, 1213, 0, 111)
    print(c1)
    print(c1.conta)