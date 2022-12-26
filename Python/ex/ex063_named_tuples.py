from collections import namedtuple

Peca_Funcao = namedtuple('peca_e_sua_funcao', ['peca', 'funcao'],
                         defaults=['Peça não informada', 'Função não informada'])


pc_do_jose = Peca_Funcao()
print(pc_do_jose)
# pc_do_motta_cabos = peca_funcao('Cabo de força', 'Trazer energia ao computador')
# pc_do_motta_placa_mae = peca_funcao('Placa Mãe AsRock', 'Administrar outras peças')
# print(pc_do_motta_cabos)
# print(pc_do_motta_placa_mae)
# print(pc_do_motta_cabos.peca)