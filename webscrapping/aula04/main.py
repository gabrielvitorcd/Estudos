import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')


content = response.content

site = BeautifulSoup(content, 'html.parser')

noticias = site.find_all('div', attrs={'class': 'feed-post-body'})





for noticia in noticias:
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    print(titulo.text)
    print(titulo['href'])   #link da postagem

    lista_noticias.append([titulo.text,titulo['href']])

    try:
        subtitle = noticias.find('div', attrs={'class':'feed-post-body-resumo'})
        if (subtitle):
            print(subtitle.text)
    except AttributeError:
        print('<nao existe subtitulo no html>')
   
    print()

news = pd.DataFrame(lista_noticias, columns=['titulo','Subtitulo'])

news.to_excel('noticias.xlsx', index=False)
