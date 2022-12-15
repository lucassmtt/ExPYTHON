import os
import json

"""pessoas = [
    {
        "nome": 'Maria',
        "sobrenome": 'Vieira',
        "idade": 19,
        "ativo": False,
        "notas": ['A', 'A+'],
        "telefones": {
            "residencial": '48 34343434',
            "celular": '47 988432132',
        },

    },
    {
        "nome": 'Joao',
        "sobrenome": 'Roberto',
        "idade": 44,
        "ativo": True,
        "notas": ['B', 'B+'],
        "telefones": {
            "resdiencial": '47 34343642',
            "celular": '48 986424221',
        },
    },
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arq_python_json')

with open(SAVE_TO, 'w') as file:
    json.dump(pessoas, file, indent=2)

print(json.dumps(pessoas, indent=2))"""

pessoas = [
    {
        "nome": 'Joelma',
        "sobrenome": 'Vieira',
        "idade": 19,
        "ativo": False,
        "notas": ['A', 'A+'],
        "telefones": {
            "residencial": '48 34343434',
            "celular": '47 988432132',
        },

    },
    {
        "nome": 'Joao',
        "sobrenome": 'Roberto',
        "idade": 44,
        "ativo": True,
        "notas": ['B', 'B+'],
        "telefones": {
            "resdiencial": '47 34343642',
            "celular": '48 986424221',
        },
    },
]

with open('aula041.json', 'w') as arquivo:
    json.dump(
        pessoas, arquivo, ensure_ascii=False, indent=2
    )

# with open('aula041.json', 'r', encoding='UTF-8') as arquivo:
#     pessoa = json.load(
#         arquivo,
#     )
#     for v in pessoa:
#         print(v['nome'])
#
# print(*pessoa, sep='\n')
