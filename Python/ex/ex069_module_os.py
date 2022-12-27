import os

# if os.path.exists('/home/lucassmtt/Documentos'):
#     os.system('mkdir LUCASDOIDAODEMAISI')
# else:
#     print('Caminho inexistente')

# caminho = os.path.join('Desktop', 'Documentos','Estudos', 'arquivo_test.txt')
#
# caminho, arquivo = os.path.split(caminho)
# # print(caminho,'-', arquivo)
#
# arquivo, extensão_do_arquivo = os.path.splitext(arquivo)
# print(arquivo, '-', extensão_do_arquivo)
#
# if os.path.exists('/home/lucassmtt/Documentos'):
#     print('LIndao')

# print(os.path.abspath(''))

caminho = os.path.join('/home/lucassmtt/Documentos/EXEMPLO_OS/')

for pasta in os.listdir(caminho):
    print('EXTERNO')
    print(pasta)
    caminho_com_pasta = os.path.join(caminho, pasta)

    if not os.path.isdir(caminho_com_pasta):
        print('Diretório impossível de acessar...')

    for pasta_interna in os.listdir(caminho_com_pasta):
        print('INTERNO')
        print('*********',pasta_interna)
        print('-'*20)


