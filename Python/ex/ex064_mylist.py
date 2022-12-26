from collections.abc import Sequence

# class MyList:
#     def __init__(self):
#         self._my_data = {}
#         self._iterator = 0
#
#     def append(self, value):
#         self._my_data[self._iterator] = value
#         self._iterator += 1
#
# if __name__ == '__main__':
#     MINHA_LISTA = MyList()
#     MINHA_LISTA.append('João')
#     MINHA_LISTA.append('Guilhereme')
#     print(MINHA_LISTA._my_data)

#o metodo acima seria fazendo uma lista própria meio "HardCode"

class MyList:
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
        new_list = MyList()
        new_list.append('Maria', 'Roberto', 'Adamastor')
        new_list.append('Jose')
        for value in new_list:
            print(value)
        new_list[0] = 'Guilherme'
        print()
        for value in new_list:
            print(value)