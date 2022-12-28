import json
# from pprint import pprint
from typing import TypedDict


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

movie: Movie = json.loads(string_json)
# print(movie['title'])
# print(movie['original_title'])
# print(movie['is_movie'])
# print(movie['imdb_rating'])
# print(movie['year'])
# print(movie['characters'])
# print(movie['budget'])

print(json.dumps(movie, ensure_ascii=False, indent=2))