"""
Faça um programa para corrigir provas de múltipla escolha com somatória.
Cada prova tem dez questões e cada questão vale 1 ponto.
O primeiro conjunto de dados a ser lido é o gabarito da prova.
Os outros dados serão os números dos alunos e sua respectivas respostas.
Existem 15 alunos matriculados. Calcule e mostre:

- Para cada aluno seu número e sua nota;
- A percentagem de aprovação, sabendo-se que a nota mínima é 6,0
"""


qtd_de_alunos = int(input('Digite quantos alunos serão avaliados: '))
qtd_de_questoes = int(input('Digite a quantidade de questões da prova: '))
gabarito = [''] * qtd_de_questoes
notas_da_turmas = [0] * qtd_de_alunos


for i in range(qtd_de_questoes):
    gabarito[i] = str(input('Defina a resposta correta para '
                            f'questão de número {i+1}: ')).upper()


#Vai passar pela quantidade de alunos
for aluno in range(qtd_de_alunos):
    resp_aluno = [''] * qtd_de_questoes

    #vai passar pela quantidade de questões
    for questao in range(qtd_de_questoes):
        print(f"""
        Questão {questao+1}: pipipipopo:
        
        A) = Pi
        B) = Pipi
        C) = Po
        D) = Popo
        
        """)

        resp_aluno[questao] = str(input(
        f'Digite sua resposta para questão número {questao+1}: '
        )).upper()


    nota = 0
    for i in range(qtd_de_questoes):
        if resp_aluno[i] == gabarito[i]:
            nota += 1
    notas_da_turmas[aluno] = nota
    print(f'Seu número é o {aluno+1} e sua nota foi de: '
          f'{nota/qtd_de_questoes*10}')


media_alunos = [0.0] * qtd_de_alunos
for i in range(qtd_de_alunos):
    media_alunos[i] = notas_da_turmas[i] / qtd_de_questoes


total_para_media = 0
for i in range(qtd_de_alunos):
    total_para_media += media_alunos[i]


media_global = total_para_media / qtd_de_alunos
print(f'A média da sala foi: {media_global * 100}% de acerto.')
