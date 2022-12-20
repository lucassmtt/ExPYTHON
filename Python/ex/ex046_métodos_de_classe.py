# class Pessoa:
#     var = 'ola'
#
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
#     @classmethod
#     def metodo_de_classe(cls):
#         print('Hey')
#
#     @classmethod
#     def bonde_de_cinquenta(cls, nome):
#         return cls(nome, 50)
#
#     @classmethod
#     def criar_sem_nome(cls, idade):
#         return cls('Anõnima', idade)
#
# pessoa01 = Pessoa.bonde_de_cinquenta('João')
# pessoa02 = Pessoa.criar_sem_nome(45)
#
# print(pessoa01.nome)
# print(pessoa01.idade)
# print()
# print(pessoa02.nome)
# print(pessoa02.idade)
#
# class Conection:
#     @classmethod
#     def create_with_auth(cls, user, password):
#         conection = cls
#         conection.user = user
#         conection.password = password
#         return conection
#
# cliente_01 = Conection.create_with_auth('Lucas', '123')
# print(cliente_01.user)
# print(cliente_01.password)


