class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def mostrar_nome(self):
        print(self.nome)

    def mostrar_salario(self):
        print(self.salario)


funcionario_numero_100 = Funcionario('João', 1122)
funcionario_numero_100.mostrar_nome()
funcionario_numero_100.mostrar_salario()