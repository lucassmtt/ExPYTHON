import math
from itertools import count
import os

def formata_tamanho(tamanha_em_bytes: int, base: int = 1024) -> str:
    if tamanha_em_bytes <= 0:
        return '0B'

    abreviacao_tamanho = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'

    indice_abreviacao_tam = int(math.log(tamanha_em_bytes, base))

    potencia = base ** indice_abreviacao_tam

    tamanho_final = tamanha_em_bytes / potencia

    abreviacao_tamanho = abreviacao_tamanho[indice_abreviacao_tam]

    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


caminho = os.path.join('/home','lucassmtt', 'Documentos', 'EXEMPLO_OS')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    caminho_root = os.path.join(caminho, root)
    # tam_arq = os.path.getsize(caminho_root)
    # print(formata_tamanho(tam_arq))
    stats = os.stat(caminho_root)
    tamanho = stats.st_size
    print(formata_tamanho(tamanho))
    print(the_counter, 'Pasta atual', root)
    for dir_ in dirs:
        caminho_do_dir = os.path.join(root, dir_)
        print('      ',the_counter, 'DIRS', dirs)
        print('CAMINHO DO DIR',dir_)