nome = str(input('Digite seu nome: '))
if 4 > len(nome) >= 1:
    print('Seu nome é pequeno!')
elif 6 > len(nome) > 4:
    print('Seu nome é medio!')
else:
    print('Seu nome é grande!')