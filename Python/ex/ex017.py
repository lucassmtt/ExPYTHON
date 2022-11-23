def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

##em versão função lambda

print(
    executa(
        lambda x, y: x + y,
        #colocar os argumentos
        2, 4
    )
)