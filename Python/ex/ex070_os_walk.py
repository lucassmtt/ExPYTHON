import os
from itertools import count


caminho = os.path.join('/home','lucassmtt', 'Documentos', 'EXEMPLO_OS')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)
    for dir_ in dirs:
        caminho_do_dir = os.path.join(root, dir_)
        print('      ',the_counter, 'DIRS', dirs)
        print('CAMINHO DO DIR',caminho_do_dir)
        os.unlink(caminho_do_dir)

os.unlink(caminho)