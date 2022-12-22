from Log import LogPrintMixin
class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

class Smartphone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()
        if not self._ligado:
            self.success(print(f'{self._nome} está ligando'))

    def desligar(self):
        super().ligar()
        if self._ligado:
            self.error(print(f'{self._nome} está desligando'))