import sys

iterable = ['Eu', 'Tenho', '__iter__'] ##iterável
iterator = iter(iterable) ##tem o __iter__ e __next__
lista = [n for n in range(0,1000000)]
generator = ((n for n in range(0,1000)))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for num in generator:
    print(num)