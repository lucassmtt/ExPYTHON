#!usr/bin/env python3
import sys
import os

args = sys.argv
qtd_args = len(args)

if qtd_args == 1:
    print('Faltando argumentos... \t')
    print('-a Para listar todos arquivos nesta pasta \t')
    print('-d Para listar todos os diretórios nesta pasta \t')
#     os.system('echo faltando args')
    sys.exit()

file_ = False
dirs_ = False

if '-a' in args:
    file_ = True

if '-d' in args:
    dirs_ = True

for dirs in os.listdir('.'):
    if os.path.isdir(dirs) and dirs_:
        print(dirs)
    if os.path.isfile(dirs) and file_:
        print(dirs)