# class Pessoa:
#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = sobrenome
#
#
# p1 = Pessoa('Lucas', 'Motta')
# p2 = Pessoa('Joao', 'Aguiar')
#
# print(p1.nome)
# print(p1.sobrenome)
# print()
# print(p2.nome)
# print(p2.sobrenome)

# class Carro:
#     def __init__(self, nome, modelo, ano):
#         self.nome = nome
#         self.modelo = modelo
#         self.ano = ano
#
#
# carro_do_lucas = Carro('Fusca', 'Hetch', 1998)
#
# print(carro_do_lucas.nome)
# print()
# print(carro_do_lucas.modelo)
# print()
# print(carro_do_lucas.ano)


# class Caneta:
#     def __init__(self):
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar_desligar(self, desligar=False):
        if desligar:
            print(f'{self.nome} desligando...')
            self.filmando = False
            print(f'{self.nome} desligada!')
            return
        elif self.filmando:
            print(f'{self.nome} ja está filmando')
            return
        else:
            print(f'{self.nome} está filmando...')
            self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'É impossível fotografar enquanto está gravando')
            return

        print(f'{self.nome} está fotografando...')

c1 = Camera('Canon')
c2 = Camera('Philco')

c1.filmar_desligar()
print()
c1.fotografar()
print()
c1.filmar_desligar(desligar=True)
print()
c1.fotografar()