class Creche:
    def __init__(self, nome_creche):
        self.quantidade_de_turmas = None
        self.nome_creche = nome_creche
        self.turmas: dict = {}
        self.qtd_de_alunos: int = 0
        self.numero_de_sala_indisponivel: [int] = []

    def novas_turmas(self, quantidade_de_turmas) -> {dict}:
        self.quantidade_de_turmas = quantidade_de_turmas

        for turma in range(self.quantidade_de_turmas):
            qtd_de_alunos_masculinos_p_turma: int = 0
            qtd_de_alunas_femininas_p_turma: int = 0

            while True:
                numero_sala = input('Digite o número de sala: ')
                if numero_sala.isnumeric():
                    int(numero_sala)
                    if numero_sala not in self.numero_de_sala_indisponivel:
                        break
                    else:
                        print('Você digitou um número de sala que já está sendo utilizado'
                              ', por favor digite outra sala que esteja disponível')
                        for sala_indisponivel in self.numero_de_sala_indisponivel:
                            print(f'Número indisponível: {sala_indisponivel}')
                else:
                    print('Por favor digite um número correto!')
            self.numero_de_sala_indisponivel.append(numero_sala)

            while True:
                qtd_alunos_turma = input('Quantas crianças tem na sala: ')
                if qtd_alunos_turma.isnumeric():
                    qtd_alunos = int(qtd_alunos_turma)
                    break
                else:
                    print('Por favor digite um número válido!')

            self.qtd_de_alunos += qtd_alunos

            for _aluno in range(qtd_alunos):
                print("""
                A criança é do sexo masculino ou feminino? 
                F = Feminino
                M = Masculino
                """)

                aluno = str(input(':')).lower().rstrip().lstrip()
                if aluno == 'm':
                    qtd_de_alunos_masculinos_p_turma += 1
                if aluno == 'f':
                    qtd_de_alunas_femininas_p_turma += 1

            nova_turma: dict = {}
            nova_turma.setdefault('Número da sala', numero_sala)
            nova_turma.setdefault('Quantidade de alunos', qtd_alunos_turma)
            nova_turma.setdefault('Quantidade de meninos',
                                  qtd_de_alunos_masculinos_p_turma)
            nova_turma.setdefault('Quantidade de meninas',
                                  qtd_de_alunas_femininas_p_turma)

            self.turmas.setdefault(f'Turma {turma}', nova_turma)

        return self.turmas

    def mostrar_total_alunos(self) -> print:
        print(f'A escola tem um total de : {self.qtd_de_alunos} alunos')

    def mostrar_media_aluno_por_sala(self) -> print:
        media_de_alunos = self.qtd_de_alunos / self.quantidade_de_turmas
        print(f'A média de aluno por sala é : {media_de_alunos}')

    def mostrar_sala_com_maior_num_meninos(self) -> print:
        turma_qtd: int = 0
        turma_com_mais_meninos: str = ''

        for i in range(self.quantidade_de_turmas):
            turma = self.turmas.get(f'Turma {i}')
            qtd_de_meninos = (turma.get('Quantidade de meninos'))

            if i == 0:
                turma_com_mais_meninos = turma.get('Número da sala')
                turma_qtd = qtd_de_meninos

            if qtd_de_meninos > turma_qtd:
                turma_com_mais_meninos = turma.get('Número da sala')
                turma_qtd = qtd_de_meninos

        print(f'A turma com mais meninos é a de número: {turma_com_mais_meninos}')

    def mostrar_sala_com_menor_num_meninas(self) -> print:
        turma_qtd: int = 0
        turma_com_menos_meninas: str = ''

        for i in range(self.quantidade_de_turmas):
            turma = self.turmas.get(f'Turma {i}')
            qtd_de_meninas = (turma.get('Quantidade de meninas'))

            if i == 0:
                turma_com_menos_meninas = turma.get('Número da sala')
                turma_qtd = qtd_de_meninas

            if qtd_de_meninas < turma_qtd:
                turma_com_menos_meninas = turma.get('Número da sala')
                turma_qtd = qtd_de_meninas

        print(f'A turma com menos meninas é a de número: {turma_com_menos_meninas}')


def clean_print(num_espacos):
    print('-' * num_espacos)


Abdon_batista = Creche('Escola de Educação Primária Abdon Batista')
Abdon_batista.novas_turmas(1)
clean_print(20)
Abdon_batista.novas_turmas(1)
clean_print(20)
Abdon_batista.mostrar_total_alunos()
clean_print(20)
Abdon_batista.mostrar_media_aluno_por_sala()
clean_print(20)
Abdon_batista.mostrar_sala_com_menor_num_meninas()
clean_print(20)
Abdon_batista.mostrar_sala_com_maior_num_meninos()
