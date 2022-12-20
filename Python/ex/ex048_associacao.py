class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Ferramenta_para_escritor:
    def __init__(self, nome_da_ferramenta):
        self.nome_da_ferramenta = nome_da_ferramenta

    def action(self):
        print(f'{self.nome_da_ferramenta} está escrevendo')

escritor_lucas = Escritor('Lucas Motta')
caneta_do_lucas = Ferramenta_para_escritor('Caneta BIC')

escritor_lucas.ferramenta = caneta_do_lucas

escritor_lucas.ferramenta.action()
