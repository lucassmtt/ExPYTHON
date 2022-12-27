from datetime import datetime
from dateutil.relativedelta import relativedelta

# hr = datetime.now(timezone('Asia/Tokyo'))
# print(hr)
#
# print(datetime.now())
# data = datetime.now()
# print(data.timestamp()) #pegar a data
# print(data.fromtimestamp(1672096994.062737)) #transformar em data legível de novo

formatacao = '%d/%m/%Y %H:%M:%S'
fmt_ano = '%Y/%m'
fmt_ano_mes_dia = '%d/%m/%Y'
fmt_tudo = '%d/%m/%Y %H:%M'
#
nascimento = datetime.strptime('02/07/2004 18:30:23' , formatacao)
data_de_hoje = datetime.now()
# data_de_hoje.strptime(fmt_ano)
minha_idade_dias = data_de_hoje - nascimento
# print(minha_idade_dias)
#
# print(data_de_hoje + relativedelta(minutes=4))
# data_relative_delta = relativedelta(nascimento, data_de_hoje)
# print(data_relative_delta)
# print(data_de_hoje.strftime(fmt_ano))
# print(data_de_hoje.strftime(fmt_ano_mes_dia))
# print(data_de_hoje.strftime(fmt_tudo))

