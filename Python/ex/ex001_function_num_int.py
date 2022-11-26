def numint(msg, msg_aviso=''):
    num = input('Digite um número inteiro: ')
    while not num.isdigit():
        print(msg)
        num = input(msg_aviso)
    num = int(num)
    return num


numero = numint(msg='ERRO', msg_aviso='DIGITE CORRETO')
if (numero % 2) == 0:
    print('Seu número é: PAR ')
else:
    print('Seu número é: IMPAR ')
