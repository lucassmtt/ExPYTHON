def soma(x, y):
    return x + y

def multiplicador(x, y):
    return x * y

def make_function(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = make_function(soma, 5)


def fora(x):
    var = x
    def dentro():
        return var
    return dentro

dentro = fora(90)

def concatenar(string_primaria):
    string_final = string_primaria
    def interna(string):
        nonlocal string_final
        string_final += string
        return string_final
    return interna

concatenando = concatenar('ALO')
print(concatenando('abu'))
print(concatenando('RODINEI'))

def inverte_str(string):
    return string[::-1]

print(inverte_str('Alo'))


def criador_decorador(a, b, c):
    def decorador(funcao, *args):
        def funcao(*args):
            