from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_inicial = 1_000_000
dt_inicial = datetime(2022, 12, 20)
delta = relativedelta(years=5)
dt_final = dt_inicial + delta


dt_parcelas = []
parcela = dt_inicial


while parcela < dt_final:
    dt_parcelas.append(parcela)
    parcela += relativedelta(months=+1)

numero_parcelas = len(dt_parcelas)
valor_parcela = valor_inicial / numero_parcelas
print(f'{valor_parcela:,.2f}')


cont_parcela = 1
fmt_ano_mes_dia = '%d/%m/%Y'
for data in dt_parcelas:
    print(f'({cont_parcela}) = {data.strftime(fmt_ano_mes_dia)} = {valor_parcela:,.2f}')
    cont_parcela += 1

