iterable = ['Eu', 'Tenho', '__iter__'] ##iterável
iterator = iter(iterable) ##tem o __iter__ e __next__
print(next(iterator))
print(next(iterator))


#generator
import sys

iterable = ['Eu', 'Tenho', '__iter__'] ##iterável
iterator = iter(iterable) ##tem o __iter__ e __next__
lista = [n for n in range(0,1000000)]
generator = ((n for n in range(0,1000)))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for num in generator:
    print(num)

##Generator Function
def generator(n=0, maximum=10):
    while True:
        if n == maximum:
            return 'Acabou'
            break
        yield n
        n += 1

gen = generator(maximum=3)
print(next(gen))
print(next(gen))
print(next(gen))print(next(gen))
print('minha irmã é muito linda, tenho outra irmã que é feia, que é a a myisabella')  