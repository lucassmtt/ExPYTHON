import requests
import re
from bs4 import BeautifulSoup

url = 'http://0.0.0.0:3333/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')

print(parsed_html.title)
print('-'* 40)
print(parsed_html.find_all('h2', limit=3))
print('-'* 40)

title_jobs = parsed_html.select_one('#intro > div > div > article > h2')
if title_jobs is not None:
    texto_do_job = title_jobs.parent

    if texto_do_job is not None:
        print(texto_do_job)
        for p in texto_do_job.select_one('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())