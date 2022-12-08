def fab_decoradores(a, b, c):
    def decoradora(function):
        def interna(*args, **kwargs):
            res = function(*args, **kwargs)
            return res
        return interna
    return decoradora


@fab_decoradores(1, 2, 4)
def soma(x, y):
    return x + y


@fab_decoradores(1, 3, 4)
def multiplica(x, y):
    return x * y


multiplica_por_mil = multiplica(1, 1000) #da para fazer desta forma

soma_com_cinco = fab_decoradores(1, 2, 4)(lambda x: x + 5) #da para fazer usando lambda

dobro_de = fab_decoradores(1, 3, 4)(lambda x: x * 2) #lambda também


print(multiplica_por_mil)
print(soma_com_cinco(5))
print(dobro_de(8))