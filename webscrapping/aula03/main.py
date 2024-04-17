import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')


content = response.content

site = BeautifulSoup(content, 'html.parser')

noticia = site.find('div', attrs={'class':'feed-post-body'})

extracao_titulo = noticia.find('a', attrs={'class':'feed-post-link'})
extracao_resumo = noticia.find('div', attrs={'class':'gui-color-primary'})
#print(noticia.prettify())
print(extracao_resumo)

titulo = extracao_titulo.text
#resumo = extracao_resumo.text

print(f'O titulo [{titulo}]')
#print(f'O resumo [{resumo}]')