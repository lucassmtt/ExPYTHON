iterable = ['Eu', 'Tenho', '__iter__'] ##iterável
iterator = iter(iterable) ##tem o __iter__ e __next__
print(next(iterator))
print(next(iterator))
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
def generator(n=0, num=0):
    while True:
        if n == num:
            return 'Acabou'
            break
        yield n
        n += 1

gen = generator(10)
for n in gen:
    print(n)