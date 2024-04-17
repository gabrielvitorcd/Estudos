import requests
from bs4 import BeautifulSoup
import pandas as pd

def linha():
    print('-'*40)

sumario_site = []
sub1 = []
sub2 = []
sub3 = []
sub4 = []


requesicao = requests.get('https://www.usecadeirinha.com.br/melhores-cadeirinhas/')

conteudo_bruto = requesicao.content

site = BeautifulSoup(conteudo_bruto,'html.parser')

linha()
h1 = site.find('h1')
print(f'H1-')
print(h1.text)
sub1.append(h1.text)
sumario_site.append(sub1)
linha()

h2 = site.find_all('h2')
print(f'H2- TOTAL {len(h2)}')
for titulo in h2:
    print(titulo.text)
    sub2.append(titulo.text)

linha()

h3 = site.find_all('h3')
print(f'H3- TOTAL {len(h3)}')
for titulo in h3:
    print(titulo.text)
    sub3.append(titulo.text)

linha()

h4 = site.find_all('h4')
print(f'H4- TOTAL {len(h4)}')
for titulo in h4:
    print(titulo.text)
    sub4.append(titulo.text)



print(df)
print(sub1)
print(sub2)
#tabela.to_excel('todoshsdosite.xlsx', index=False)


