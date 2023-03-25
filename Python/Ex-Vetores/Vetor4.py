"""
Exercício Proposto:

Faça um programa que receba a temperatura
média de cada mês do ano e armazene-as em um vetor.
Calcule e mostre a maior e a menor temperatura do ano e em que mês elas
ocorreram (mostrar o mês por extenso: 1- Janeiro, 2 – Fevereiro).
Desconsidere empates.

"""
mes_mais_frio = ''
mes_mais_quente = ''
temp_mais_frio = 0
temp_mais_quente = 0


meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
meses_em_graus = [0] * 12


for i in range(12):
    #Recebimento da temperatura de cada mês
    meses_em_graus[i] = int(input(
        f'Digite a temperatura média do mês de {meses[i]}: '
    ))


for i in range(12):
    #Considera o primeiro valor o maior e o menor das temperaturas
    if i == 0:
        temp_mais_quente = meses_em_graus[i]
        temp_mais_frio = meses_em_graus[i]
        mes_mais_quente = meses[i]
        mes_mais_frio = meses[i]

    #Processamento da temperatura mais fria
    if temp_mais_frio > meses_em_graus[i]:
        temp_mais_frio = meses_em_graus[i]
        mes_mais_frio = meses[i]

    #Processamento da temperatura mais quente
    if temp_mais_quente < meses_em_graus[i]:
        temp_mais_quente = meses_em_graus[i]
        mes_mais_quente = meses[i]


print(
    f'O mês mais frio foi o mês de {mes_mais_frio} com uma temperatura'
    f' de {temp_mais_frio}ºC.'
)

print(
    f'O mês mais quente foi o mês de {mes_mais_quente} com uma temperatura'
    f' de {temp_mais_quente}ºC.'
)