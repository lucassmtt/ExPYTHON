def make_func(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
            if isinstance(arg, str):
                print('è uma string')
        return func(*args, **kwargs)
    return interna

@make_func
def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser string')


inverte_string_checando = make_func(inverte_string)
invertida = inverte_string_checando('123')
print(invertida)