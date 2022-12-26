from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta

# hr = datetime.now(timezone('Asia/Tokyo'))
# print(hr)
#
# print(datetime.now())
# data = datetime.now()
# print(data.timestamp()) #pegar a data
# print(data.fromtimestamp(1672096994.062737)) #transformar em data legível de novo

formatacao = '%d/%m/%Y %H:%M:%S'
#
nascimento = datetime.strptime('02/07/2004 18:30:23' , formatacao)
data_de_hoje = datetime.now()
minha_idade_dias = data_de_hoje - nascimento
print(minha_idade_dias)

print(data_de_hoje + relativedelta(minutes=4))
data_relative_delta = relativedelta(nascimento, data_de_hoje)
print(data_relative_delta)