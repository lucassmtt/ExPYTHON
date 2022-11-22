perguntas = [
    {
        'Pergunta': 'Quanto é 30*30?',
        'Opções': ['300', '400', '900'],
        'Resposta': '900'
    },
    {
        'Pergunta': 'Qual é considerado o melhor jogador de todos os tempos de futebol? ',
        'Opções': ['R10', 'Messi', 'Ronaldo', 'Pelé'],
        'Resposta': 'Pelé'
    },
    {
        'Pergunta': 'Qual é considerado o melhor jogador de todos os tempos de basquete? ',
        'Opções': ['Jordan', 'Jordan Poll', 'Curry', 'Lebron James'],
        'Resposta': 'Jordan'
    }
]

for pergunta in perguntas:
    resp = ''
    print(pergunta['Pergunta'])
    cont = 1
    for opc in pergunta['Opções']:
        print(f'{cont}) = {opc}')
        cont += 1
    resp = str(input('Digite sua resposta: '))
    if resp == pergunta['Resposta']:
        print('Você acertou!')
    else:
        print('Você errou! ')
        print(f'A resposta correta era {pergunta["Resposta"]}')