# def ola(nome):
#     def func_interna(nome):
#         if nome.lower() == 'mariele':
#             print(f'Olá {nome}. A noite, tainha, vinho e muito...')
#
#         else:
#             print(f'Olá {nome}, boas vindas')
#     func_interna(nome)
#
# ola('mariele')

#
# def normaliza(*palavras):
#     saida = []
#
#     for palavra in palavras:
#         normalizado = normalize('NFKD', palavra)
#         normalizada = normalizado.encode('ASCII', 'ignore').decode('ASCII')
#         saida.append(normalizada)
#
#     return saida
#
# print(normaliza('Érico, Sabiá, João'))

# from unicodedata import normalize
#
# def normaliza(*palavras):
#
#     def ajudante(palavra):
#         normalizado = normalize('NFKD', palavra)
#         return normalizado.encode('ASCII', 'ignore').decode('ASCII')
#
#     return [ajudante(palavra) for palavra in palavras]
#
# print(normaliza('Érico, Sabiá, João'))


# def soma_x(val_externo):
#     def interna(val_interno):
#         return val_externo + val_interno
#     return interna
#
#
# soma_1 = soma_x(1)
# soma_10 = soma_x(10)
#
# print(soma_1(10))

def contador(start=0):
    count = start

    def interna():
        count += 1
        return count

    return interna

c = contador()
print(c())