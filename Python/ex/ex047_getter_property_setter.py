# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor
#
#     def get_cor(self):
#         return self.cor_tinta
#
#
# caneta_bic = Caneta('Amarela')
# print(caneta_bic.get_cor())

class Caneta:
    def __init__(self, cor):
        self.__cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        if self.__cor == 'rosa':
            print('Proibido cor rosa')
            return
        return self.__cor

    @cor.setter
    def cor(self, valor):
        if self.__cor == 'rosa':
            print('proibido cor rosa')
        self.__cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


c1 = Caneta('Azul')
c1.cor_tampa = 'Amarela'
print(c1.cor_tampa)