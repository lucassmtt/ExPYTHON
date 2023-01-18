from threading import Thread
from threading import Lock
from time import sleep

# class myThread(Thread):
#     def __init__(self, text, time):
#         self.text = text
#         self.time = time
#
#         super().__init__()
#
#     def run(self):
#         sleep(self.time)
#         print(self.text)
#
# first_thread = myThread('Hello, world', 0.7)
# first_thread.start()
#
# seccond_thread = myThread('Hi, world', 3)
# seccond_thread.start()
#
# tree_thread = myThread('Good bye, world', 4)
# tree_thread.start()
# for i in range(10):
#     print(i)
#     sleep(1)

# def _sleeping_(text, time):
#     sleep(time)
#     print(text)
# #
# # t = Thread(_sleeping_('Hello, world', 3))
# # t.start()
#
# my_thread = Thread(target=_sleeping_, args=('Hello, world', 5))
# my_thread.start()
#
# cont = 0
# while my_thread.is_alive():
#     print(f'Esperando minha thread acabar... {cont}')
#     sleep(1)
#     cont += 1
#
# print(cont)

class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire() #faz esperar a execução

        if self.estoque >= quantidade:
            self.estoque -= quantidade
            print(f'Você comprou {quantidade} ingresso(s),'
                  f' ainda temos {self.estoque}')
        else:
            print('Impossível comprar, o estoque acabou')

        self.lock.release()#libera a execução para outra invocação

if __name__ == '__main__':
    bilheteria_frontal = Ingresso(10)

    for compra in range(1, 10):
        t = Thread(target=bilheteria_frontal.comprar, args=(compra,))
        t.start()

    print(bilheteria_frontal.estoque)