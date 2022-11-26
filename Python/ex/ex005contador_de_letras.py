frase = 'aaabbb'
i = 0
letra_apereceu_mais = ''
quantidade_letra = 0

while i < len(frase):
    index_letra = frase[i]
    quantidade_letra_index = frase.count(index_letra)
    if frase[0] == 0:
        quantidade_letra = quantidade_letra_index
        letra_apereceu_mais = index_letra
    if index_letra == ' ':
        i += 1
        continue
    if quantidade_letra < frase.count(index_letra):
        quantidade_letra = quantidade_letra_index
        letra_apereceu_mais = index_letra
    i += 1

print(f'A letra que apareceu mais foi {letra_apereceu_mais}, aparecendo {quantidade_letra} vezes.')