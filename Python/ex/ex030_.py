def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = criar_funcao(soma, 5)
multiplicador_por_dez = criar_funcao(multiplica, 10)
print(soma_com_cinco(3))