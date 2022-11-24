pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Motta'
}

dados_pessoas = {
    'idade': 19,
    'altura': 1.8,
}

pessoa_completa = {**pessoa, **dados_pessoas, 'chave': 1 }

print(pessoa_completa)

def mostra_args_nomeados(*args, **kwargs):
    print(kwargs)

mostra_args_nomeados(nome='Joana', ql1=123)