a = 18
b = 0
try:
    c = a / b
except ZeroDivisionError:
    print('Não deu porque b não tem valor')
##se colocar um "as" depois da exceção temos uma variável para tela