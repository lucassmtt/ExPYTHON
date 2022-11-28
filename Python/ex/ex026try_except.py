def divison(n, d):
    if d == 0:
        raise ZeroDivisionError('Voce tentou dividir um número por zero')
    return n / d


print(divison(4, 0))