class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def mostrar_nome(self):
        print(self.nome)

    def mostrar_salario(self):
        print(self.salario)

    def aumentar_salario(self, valor_em_porcentagem):
        self.salario += (self.salario * valor_em_porcentagem / 100)


funcionario_numero_100 = Funcionario('Marcos', 1000)
funcionario_numero_100.mostrar_nome()
funcionario_numero_100.mostrar_salario()
funcionario_numero_100.aumentar_salario(10)
funcionario_numero_100.mostrar_salario()

