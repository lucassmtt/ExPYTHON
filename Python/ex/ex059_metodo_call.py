class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwargs):
        if kwargs:
            nome = [v for v in kwargs.values()]
            print(f'{nome[0]} está te ligando...')
        else:
            print(f'Telefone desconhecido está te ligando')

telefone_luan = CallMe(195348003)
telefone_luan()