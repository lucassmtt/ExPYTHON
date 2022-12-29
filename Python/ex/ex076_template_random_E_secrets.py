# import secrets
# import string as s
# from secrets import SystemRandom as Sr
#
# print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=20)))

#template string

import locale
import string
from datetime import datetime
from pathlib import Path


CAMINHO = Path(__file__).parent / 'ex076_template.txt'

#podemos buscar um texto fora do __main__, ou deixar ele em forma de docstring

# texto_template = '''
# Prezado(a) %nome,
#
# Informamos que sua mensalidade será cobrada no valor de %{valor} no dia %data.
# Caso deseje cancelar o serviço, entre em contato com a %empresa pelo telefone %telefone.
#
# Atenciosamente,
#
# %{empresa},
# '''

locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(valor: float) -> str:
    brl = 'R$'+ locale.currency(valor, symbol=False, grouping=True)
    return brl

data = datetime(2022, 3, 29)

dados = dict(
    nome='Luan',
    valor=converte_para_brl(100831830),
    data= data.strftime('%d/%m/%Y'),
    empresa='Lucas Motta',
    telefone='+55 47 991808892'
)

class MyTemplate(string.Template):
    delimiter = '%' #DELIMITADOR DO TEMPLATE NO TEXTO
#
# template = MyTemplate(texto_template)
# print(template.substitute(dados))

with open(CAMINHO, 'r') as arquivo:
    texto_template = arquivo.read()
    template = MyTemplate(texto_template)
    print(template.substitute(dados))
