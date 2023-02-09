from functools import partial

def soma(x, y):
    return x + y

soma_com_10 = partial(soma, 10)

print(soma_com_10(10))