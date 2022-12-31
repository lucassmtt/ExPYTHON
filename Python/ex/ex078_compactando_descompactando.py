from zipfile import ZipFile
from pathlib import Path


CAMINHO_ARQ = Path.home() / 'ARQUIVOS'
CAMINHO_ARQ.touch(exist_ok=True)
print(CAMINHO_ARQ)


with ZipFile('arquivo.zip', 'w') as zip:
    for dir_ in Path.iterdir(CAMINHO_ARQ):
        CAMINHO_DIR = Path.joinpath(dir_)
        zip.write(CAMINHO_DIR, dir_.parts[4])


with ZipFile('arquivo.zip', 'r') as zip:
    for dir_ in zip.namelist():
        print('-----')
        print(dir_)


with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('arq_descompactados')
