lista = []
dicicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'thuthy'

print(f'TESTE', falsy('TESTE'))

string = 'Lucas'

if hasattr(string, 'upper'):
    print('Tem o método upper')
    print(string.upper())

metodo = 'upper'
