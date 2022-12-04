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
    def interna