import json
import os
#
#
# NOME_ARQ = 'aulaex074.json'
# ABSOLUTO = os.path.abspath(
#     os.path.join(
#         os.path.dirname(__file__), NOME_ARQ
#     )
# )
#
#
# string_json ={
#   "title": "O Senhor dos Anéis: A Sociedade do Anel",
#   "original_title": "The Lord of the Rings: The Fellowship of the Ring",
#   "is_movie": True,
#   "imdb_rating": 8.8,
#   "year": 2001,
#   "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
#   "budget": None
# }
#
# with open(ABSOLUTO, 'w', encoding='UTF8') as arquivo:
#     json.dump(string_json, arquivo, indent=2, ensure_ascii=False)
#
# with open(ABSOLUTO, 'r+', encoding='UTF8') as arquivo:
#     movie = json.load(arquivo)
#     print(movie)