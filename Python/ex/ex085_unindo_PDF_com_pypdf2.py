import PyPDF2
import os

# CAMINHO_PDF = 'pdf'

# novo_pdf = PyPDF2.PdfMerger()
#
# for root, dirs, files in os.walk(CAMINHO_PDF):
#     for file in files:
#         path_pdf_complete = os.path.join(root, file)
#
#         with open(path_pdf_complete, 'rb') as arq:
#             novo_pdf.append(arq)
#
#
# with open(f'{CAMINHO_PDF}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
#     novo_pdf.write(meu_novo_pdf)

# with open('pdf/novo_arquivo.pdf', 'rb') as arquivo:
#     reader = PyPDF2.PdfReader(arquivo)
#     num_pags = len(reader.pages)
#     # print(num_pags)
#
#     for pag in range(num_pags):
#         print(pag)
#         writer = PyPDF2.PdfWriter()
#         # pagina_atual = writer.getPage(pag) //Deprecated
#         pagina_atual = writer.pages


##Modulo muito antigo, maioria dos métodos estão depreciados 