import PyPDF2
import os

CAMINHO_PDF = 'pdf'

novo_pdf = PyPDF2.PdfMerger()

for root, dirs, files in os.walk(CAMINHO_PDF):
    for file in files:
        path_pdf_complete = os.path.join(root, file)

        with open(path_pdf_complete, 'rb') as arq:
            novo_pdf.append(arq)


with open(f'{CAMINHO_PDF}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)