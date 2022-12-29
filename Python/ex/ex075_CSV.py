import csv
from pathlib import Path

# CAMINHO_ARQUIVO_CSV = Path(__file__).parent / 'ex075.csv'


# with open(CAMINHO_ARQUIVO_CSV, 'r+', encoding='UTF8') as arquivo:
#     reader = csv.reader(arquivo)
#     for item in reader:
#         print(item)

# with open(CAMINHO_ARQUIVO_CSV, 'r', encoding='UTF8') as arquivo:
#     dreader = csv.DictReader(arquivo)
#
#     for i in dreader:
#         print(i['Nome'])
#

NOVO_ARQUIVO_CSV = Path(__file__).parent / 'aulaex074(DUMP).csv'
Path.touch(NOVO_ARQUIVO_CSV, exist_ok=True)
#
# lista_clientes = [
#     {'Nome': 'Lucas', 'Sobrenome': 'Motta'},
#     {'Nome': 'João', 'Sobrenome': 'Martins'},
#     {'Nome': 'Maria', 'Sobrenome': 'Helena'},
# ]
#
#
# with open(NOVO_ARQUIVO_CSV, 'w') as arquivo:
#     writer = csv.writer(arquivo)
#     writer.writerow(lista_clientes[0].keys())
#
#     for item in lista_clientes:
#         print(f'{item.values()} jogando este item para dentro do csv')
#         writer.writerow(item.values())


lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]


with open(NOVO_ARQUIVO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    writer = csv.DictWriter(
        arquivo, fieldnames=nome_colunas
    )
    writer.writeheader()
    for cliente in lista_clientes:
        print(f'Adicionando {cliente}')
        writer.writerow(cliente)



