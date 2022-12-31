import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for question in html.select('.s-post-summary.js-post-summary'):
    title = question.select_one('.s-link')
    date = question.select_one('.relativetime')
    wishes = question.select_one('.s-post-summary--stats-item-number')
    print(title.text, sep='\n')
    print(date.text, sep='\n')
    print(wishes.text, sep='\n')
    print('-'*50)