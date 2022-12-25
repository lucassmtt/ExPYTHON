# class MyReprMixin:
#     def __repr__(self):
#         nome_classe = self.__class__.__name__
#         nome_dict = self.__dict__
#         class_repr = f'{nome_classe}({nome_dict})'
#         return class_repr
#
#

# def meu_repr(self):
#     class_name = self.__class__.__name__
#     class_dict = self.__dict__
#     name_dict = f'{class_name}({class_dict})'
#     return name_dict
#
#
# def add_repr(classe_repr):
#     classe_repr.__repr__ = meu_repr
#     return classe_repr
#
#
# #syntax sugar, usando decorador
# @add_repr
# class Country:
#     def __init__(self, name_country):
#         self.name_country = name_country
#
# #ou usando a prórpia função decoradora
# #Country = add_repr(Country) <- desta forma
#
# BRASIL = Country('Brasil')
#
# print(BRASIL)

#
# def decoradora(funcao):
#     def interna(*args, **kwargs):
#         retorno = funcao(*args, **kwargs)
#         print('Olá mundo')
#         for arg in args:
#             print(arg)
#         return retorno
#     return interna
#
#
# @decoradora
# def mostrar_numeros(*args):
#     print(args)
#
#
# numero = mostrar_numeros(1, 3, 4)

