"""
Descrição do exercício:
Cada espectador de um cinema respondeu a um questionário no qual constava sua idade
 e a sua opinião em relação ao filme: ótimo – 3, bom – 2, regular – 1.
 Faça um programa que receba a idade e a opinião de 15 espectadores e que calcule e mostre:
- a média das idades das pessoas que responderam ótimo
- a quantidade de pessoas que respondeu regular
- a percentagem de pessoas que respondeu bom entre todos os espectadores analisados
"""
def valida_opc(msg, msg_error):
    while True:
        opc = int(input(msg))
        if opc == 1 or opc == 2 or opc == 3:
            break
        else:
            print(msg_error)


qtd_regular = 0

idade_pessoas_otimo = 0
qtd_pessoas_responderam_otimo = 0
media_otimo = 0

qtd_bom = 0
qtd_de_espectadores = int(input('Qual é a quantidade de espectadores? '))


for i in range(qtd_de_espectadores):
    idade = int(input('Digite sua idade'))
    print("""

        (1) = Regular
        (2) = Bom
        (3) = Ótimo

    """)

    opc = valida_opc('Digite uma opção: ', 'Opção inválida, digite uma opção correta!')
    if opc == 1:
        qtd_regular += 1
        break

    if opc == 2:
        qtd_bom += 1
        break

    if opc == 3:
        idade_pessoas_otimo += idade
        qtd_pessoas_responderam_otimo += 1
        break


if qtd_pessoas_responderam_otimo > 0:
    media_otimo = idade_pessoas_otimo / qtd_pessoas_responderam_otimo

porcentagem_bom = (qtd_bom / qtd_de_espectadores) * 100

print(f'A média da idade das pessoas que responderam ótimo foi igual a {media_otimo}.')
print(f'A quantidade de pessoas que respondeu regular foi {qtd_regular}.')
print(f'A porcentagem de pessoas que respondeu bom foi de {porcentagem_bom:.0f}%.')

