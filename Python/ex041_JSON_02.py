import json

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Motta',
    'adreess': [
        {'rua': 'Angolania', 'numero': 344},
        {'rua': 'Cegonhas', 'numero': 450},
    ],
    'altura': 1.76,
    'dev': True,
    'nada': None
}

with open('/home/lucassmtt/Documentos/Estudos/ExPYTHON/Python/ex/aula041.json', 'w') as arquivo:
    json.dump(pessoa, arquivo)