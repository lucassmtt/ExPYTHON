from dataclasses import dataclass, field

# @dataclass(init=False, repr=True)
# class Aviao:
#     def __init__(self, nome_motor, nome_aviao):
#         self.nome_motor: str = nome_motor
#         self.nome_aviao: str = nome_aviao
#
#
# modelo_novo = Aviao('MV8', 'Boing747')
# print(modelo_novo)

@dataclass
class Pessoa:
    nome: str = 'Missing'
    sobrenome: str = 'Not sent'
    idade: int = 0
    enderecos: list[int] = field(default_factory=list)#é obrigatório usar o field
                                                    #para colocar um arg nomeado
                                                    #obs: ela criará uma nova lista
                                                    #sempre que for chamada

if __name__ == '__main__':
    pessoa_01 = Pessoa()
    print(pessoa_01)

