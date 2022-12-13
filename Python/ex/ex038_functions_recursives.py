##exemplo de funções recursivas...

def fatorial(n):
    if n <= 1:
        return 1

    return n * fatorial(n -1)

print(fatorial(10))
print(fatorial(3))