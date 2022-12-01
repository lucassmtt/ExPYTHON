try:
    import sys 
    sys.path.append('/home')
except ModuleNotFoundError:
    print('Modulo não funciona')

print('Este modulo se chama', __name__)
print(*sys.path, sep='\n')