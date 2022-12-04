def soma(x, *args):
    res = 0
    for c in args:
        res += c
    return res + x

def multiplica(x, *args):
    res = 1
    for c in args:
        res *= c
    return res * x

def criar_funcao(funcao, *args):
    x = args[0]
    def interna(*args):
        funcao(x, args)
    return interna

multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez)