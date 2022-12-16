import os


tarefas = []
tarefas_refazer = []

def listar(tarefas):
    if not tarefas:
        print('Não possui tarefas a listar ')
        return

    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('Não possui tarefas a desfazer...')
        return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)


def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('Não possui tarefas a refazer...')
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)


def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não diigitou nenhuma tarefa')
        return

    tarefas.append(tarefa)
    return


def underline(n):
    return print('-'*n)


while True:
    print('COMANDOS: Listar, Desfazer, Refazer')
    tarefa = input('Digite um comando ou uma tarefa para fazer: ')

    if tarefa == 'listar':
        underline(30)
        listar(tarefas)
        underline(30)

    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        underline(30)
        listar(tarefas)
        underline(30)

    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        underline(30)
        listar(tarefas)
        underline(30)

    elif tarefa == 'clear':
        os.system('clear')

    else:
        adicionar(tarefa, tarefas)
        underline(30)
        listar(tarefas)
        underline(30)