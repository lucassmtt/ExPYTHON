import json
def abrir(arquivo, classes):
    dados = []
    try:
        with open(arquivo, 'r+', encoding='UTF8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print('Arquivo não existente...')
        salvar_criar(arquivo, classes)


def salvar_criar(arquivo, classes):
    dados = classes
    with open(arquivo, 'w+', encoding='UTF8') as arquivo:
        dados = json.dump(classes, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'classes.json'
classes = abrir(CAMINHO_ARQUIVO, [])
class Camera:
    def __init__(self, nome, filmando=False, fotografando=False):
        self.nome = nome
        self.fotografando = fotografando
        self.filmando = filmando

    def filmar(self):
        if self.fotografando:
            print(f'Impossível filmar. Função de fotografia ativa')
            while True:
                resp = input('Gostaria de desativar? (s)im / (n)ao').strip().lower()[0]
                if resp == 's':
                    print('Função de fotografia desativada')
                    self.fotografando = True
                    print(f'{self.nome} está fotografando...')
                    break
                if resp == 'n':
                    print('Fotografando...')
                    break
        else:
            self.filmando = True
            print(f'{self.nome} está filmando')
        return

    def fotografar(self):
        if self.filmando:
            print(f'Impossível fotografar, função de filmagem ativa')
            resp = ''
            while True:
                resp = input('Gostaria de desativar? (s)im / (n)ao').strip().lower()[0]
                if resp == 's':
                    print('Função de filmagem desativada')
                    self.filmando = True
                    print(f'{self.nome} está fotografando...')
                    break
                if resp == 'n':
                    print('Filmando...')
                    break
        else:
            self.fotografando = True
            print('A camera está fotografando...')
        return


camera_lucas = Camera('Cannon')
camera_lucas.fotografar()

salvar_criar(CAMINHO_ARQUIVO, [vars(camera_lucas)])
