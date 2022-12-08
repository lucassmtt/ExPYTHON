from itertools import groupby

alunos = [
    {'nome': 'Lucas', 'Nota': 'A'},
    {'nome': 'Anderson', 'Nota': 'B'},
    {'nome': 'Mylena', 'Nota': 'C'},
    {'nome': 'João', 'Nota': 'A'},
    {'nome': 'Gabriella', 'Nota': 'D'},
    {'nome': 'Jhou', 'Nota': 'A'},
]

def ordena(item):
    return item['Nota']


lista_correta = sorted(alunos, key=ordena)
grupos = groupby(lista_correta, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
    print('-'*40)