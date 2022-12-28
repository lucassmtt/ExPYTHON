import os
import shutil


HOME = os.path.expanduser('~')
DOC = os.path.join(HOME, 'Documentos')
PASTA_ORIGINAL = os.path.join(DOC, 'NOVA_PASTA_')
NOVA_PASTA_ = os.path.join(DOC, 'NOVA_PASTA_')

# shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA_)

shutil.move(PASTA_ORIGINAL, PASTA_ORIGINAL + 'OLA')

# os.makedirs(NOVA_PASTA, exist_ok=True)
#
#
# for root_, dirs_, files_ in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs_:
#         caminho_nova_pasta = os.path.join(
#             root_.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )
#         os.makedirs(caminho_nova_pasta, exist_ok=True)
#
#     for file in files_:
#         caminho_arquivo = os.path.join(root_, file)
#         caminho_novo_arquivo = os.path.join(
#             root_.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#         )
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)