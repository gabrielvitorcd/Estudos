import requests
from bs4 import BeautifulSoup

requesicao = requests.get('https://www.usecadeirinha.com.br/melhores-cadeirinhas/')

conteudo_bruto = requesicao.content

site = BeautifulSoup(conteudo_bruto,'html.parser')

titulos = site.find_all('h2')

for titulo in titulos:
    texto = titulo.find('span')

    print(texto.text)