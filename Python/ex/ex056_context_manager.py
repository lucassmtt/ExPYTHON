from contextlib import contextmanager

# class MyOpenFolders:
#     def __init__(self, caminho_arquivo, modo, texto):
#         self.caminho = caminho_arquivo
#         self.modo = modo
#         self._arquivo = None
#         self.texto = texto
#
#     def __enter__(self):
#         print('Abrindo Arquivo')
#         self._arquivo = open(self.caminho, self.modo, encoding='UTF8')
#         self._arquivo.write(self.texto)
#         self._arquivo.write('\n')
#
#     def __exit__(self, class_exception_, exception_, traceback_):
#         print('Fechando Arquivo')
#         self._arquivo.close()
#
# # instancia = MyOpenFolders('context_manager.json', 'w')
# # #with open(instancia)
# # #ou
#
# with MyOpenFolders('GerenciadorDeArq.txt', 'w', 'Ola mundo'):
#     ...
@contextmanager
def my_open(caminho_arquivo, modo, texto):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='UTF8')
        arquivo.write(texto)
        yield arquivo

    except Exception as e:
        print('Erro ', e)

    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('context_manager.json', 'w+', 'Olá família') as arquivo:
    arquivo.write('Ola', 123)