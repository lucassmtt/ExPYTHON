#object > classe_normal
#
# class Foo:
#     ...
# f1 = Foo()
#ou podemos criar usando o type()

# Foo = type('Foo',(object,), {})
# f1 = Foo()
# print(type(Foo))
# print(type(f1))

def meu_repr(self):
    return f'{self.__class__.__name__}({self.__dict__})'

class Meta(type):
    def __new__(mcs, name, bases, dct):
        # print('Metaclass new')
        # print('Criarei a classe abaixo...')
        random_class = super().__new__(mcs, name, bases, dct)
        random_class.attr = 'Ola, mundo'#voce pode adicionar atributos na classe...
        random_class.bom_dia = 'Bom dia, mundo'# esses atributos funcionaram para todas que herdam dela
        random_class.__repr__ = meu_repr #você pode adicionar funcionalidades também, como o __repr__
        if 'falar' not in random_class.__dict__ or not callable(random_class.__dict__['falar']):
            raise NotImplementedError('Implementação não foi criada...')
            # você pode chegar se uma implementaçao foi ou não criada
        return random_class

    def __call__(self, args='', **kwargs):
        if args == '':
            print('Indefinido')
        elif args[0] == 'Lucas':
            print('É o dono do computador')
        else:
            print(f'Bem vindo {args[0]}')

        print(f'self = {self}, args = {args}, kwargs = {kwargs}')
        return self, args, kwargs



# A metaclasse ela cria uma "instância" que no caso seria a classe "Pessoa" abaixo
class Pessoa(metaclass=Meta):       #(object, metaclass=type) por padrão são essas config iniciais
    def __new__(cls, *args, **kwargs):
        # print('Olha, o new')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        # print('Meu init')
        self.nome = nome

    def falar(self):
        return f'Olá {self.nome}'

pessoa_01 = Pessoa('Joao')