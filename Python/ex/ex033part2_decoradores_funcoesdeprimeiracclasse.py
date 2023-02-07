#funcoes de primeira classe -> são funções que são objetos
#assim como tudo nessa linguagem, podendo ser atribuidas
#para qualquer variável

lista_de_funcoes = []
lista_de_funcoes.append(lambda x, y: x-y)
lista_de_funcoes.append(lambda x, y: x-y)
lista_de_funcoes.append(lambda x, y: x*y)
lista_de_funcoes.append(lambda x, y: x/y)

funcao_tres = lista_de_funcoes[3]
print(funcao_tres(10, 5))

def soma(x, y):
    return x + y

def subtração(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def calculadora(op, x, y):
    operacoes = {
        '+':soma,
        '-':subtração,
        '*':multiplicacao,
        '/':divisao,
    }
    return operacoes[op](x, y)

def calculadora_em_lambda(op, x, y):
    operadores = {
        '+':lambda x, y: x + y,
        '-':lambda x, y: x - y,
        '*':lambda x, y: x * y,
        '/':lambda x, y: x / y,
    }
    return operadores[op](x, y)
