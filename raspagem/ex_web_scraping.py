import requests
from bs4 import BeautifulSoup

url = 'https://izilife.com.br'

response = requests.get(url)

raw_html = response.text

parsed_html = BeautifulSoup(raw_html, 'html.parser')

best_products = parsed_html.select_one('html')
links = []
if best_products is not None:

    for i in best_products.select('img'):
        links.append(i.text)

print(links)