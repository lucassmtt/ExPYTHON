# class Pessoa:
#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = sobrenome
#
#     def falar_nome_classe(self):
#         print(self.__class__.__name__)
#
# class Cliente(Pessoa):
#     ...
#
# class Aluno(Pessoa):
#     ...
#
# cliente_01 = Cliente('Lucas', 'Motta')
# cliente_01.falar_nome_classe()
#
# print('-'*30)
#
# aluno_01 = Aluno('Gabriel', 'Freitas')
# # aluno_01.falar_nome_classe()
#
# help(Aluno)

# class MinhaString(str):
#     def upper(self):
#         print('Chamada upper com o super()')
#         #return super().upper()
#         return super(MinhaString, self).upper()
#
#
# string = MinhaString('Minha nova string')
#
# print(string.upper())

class A(object):
    def metodo(self):
        print('A')

class B(A):
    def metodo(self):
        print('B')
        return super(A, self)

class C(B):
    def metodo(self):
        return super(B, self)


C = C()
print(C.metodo())