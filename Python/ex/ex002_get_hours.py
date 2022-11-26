today = list()

###horário vazio
horario = '00*00'


###horário para comparação
horarioa = '00:00'




###Vai comparar os dois horários
while not horario[2] == horarioa[2]:
    horario = str(input('Digite a hora (Formato 24hrs)'))
    print('Por favor digite ":" depois da hora')

#Adiciona dentro do dia
for c in horario:
    print(c)
    today.append(c)
print(today)

#contatena os horários
hora = int(today[0] + today[1])
minuto = int(today[3] + today[4])
horario = str(hora) + ':' + str(minuto)

#verifica a hora do dia
print(horario)
if 12 > hora > 6:
    print(f'Bom dia, agora são {horario}')
elif hora < 18:
    print(f'Boa tarde, agora são {horario}')
elif hora < 23 and minuto < 59:
    print(f'Boa noite, agora são {horario}')
else:
    print(f'Você deveria ta dormindo, agora são {horario}')