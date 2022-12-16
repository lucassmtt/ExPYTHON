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
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('Não possui tarefas a refazer...')
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    listar(tarefas)


def adicionar(tarefa, tarefas):
    if not tarefa:
        print('Você não diigitou nenhuma tarefa')
        return

    tarefas.append(tarefa)
    listar(tarefas)



def underline(n):
    return print('-'*n)


# while True:
#     print('COMANDOS: Listar, Desfazer, Refazer')
#     tarefa = input('Digite um comando ou uma tarefa para fazer: ')
#
#     if tarefa == 'listar':
#         underline(30)
#         listar(tarefas)
#         underline(30)
#
#     elif tarefa == 'desfazer':
#         desfazer(tarefas, tarefas_refazer)
#         underline(30)
#         listar(tarefas)
#         underline(30)
#
#     elif tarefa == 'refazer':
#         refazer(tarefas, tarefas_refazer)
#         underline(30)
#         listar(tarefas)
#         underline(30)
#
#     elif tarefa == 'clear':
#         os.system('clear')
#
#     else:
#         adicionar(tarefa, tarefas)
#         underline(30)
#         listar(tarefas)
#         underline(30)

#fazer desta outra forma
while True:
    print('Comandos: listar, desfazer, refazer, clear(limpar) ')
    tarefa = input('Digite um comando ou uma tarefa: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas)

    }
    # if comandos.get(tarefa) is not None:
    #     comando = comandos.get(tarefa)
    #     comando()
    # else:
    #     comando = comandos['adicionar']
    #     comando()

    #Ou desta forma

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
