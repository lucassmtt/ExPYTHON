import json
import os


NOME_ARQ = 'aulaex074.json'
ABSOLUTO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), NOME_ARQ
    )
)

print(NOME_ARQ)
print(ABSOLUTO)