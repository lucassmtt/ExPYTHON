import json


def listar(tarefas):
    if not tarefas:
        print('Não existe tarefas para listar!')
    print('TAREFAS:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')

def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('Não existe tarefas para desfazer!')
        return
    tarefa = tarefas.pop()
    print(f'{tarefa} removida da lista')
    tarefas_refazer.append(tarefa)
    underline(30)
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('Não existe tarefas para refazer!')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    underline(30)
    listar(tarefas)

def adicionar(tarefa):
    if not tarefa:
        print('Não existe tarefa para adicionar')
    tarefas.append(tarefa)
    underline(30)
    listar(tarefas)


def underline(n):
    return print(n*'_')


def ler_tarefas(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print('Arquivo não existe...')
        salvar(tarefas, caminho_arquivo)

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)
    return dados


CAMINHO_ARQUIVO = 'tarefas.json'


tarefas = ler_tarefas([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    underline(30)
    print('COMANDOS: Listar, desfazer, refazer')
    tarefa = input('Digite um comando ou uma tarefa a realizar: ')
    comandos = {
        'listar': lambda : listar(tarefas),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'adicionar': lambda: adicionar(tarefa)
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)