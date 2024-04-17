import requests
from bs4 import BeautifulSoup


url_base = 'https://lista.mercadolivre.com.br/'
produto_nome = input('Qual produto voce deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.find_all('div', attrs={'class':'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})


for produto in produtos:

    titulo = produto.find('h2', attrs={'class':'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-item__group__element'})

    real = produto.find('span', attrs={'class':'andes-money-amount__fraction'})
    centavos = produto.find('span', attrs={'andes-money-amount__cents andes-money-amount__cents--superscript-16'})



    #print(produto.prettify())
    print('Titulo do produto: ', titulo.text)
    print('Link do produto: ', link['href'])
    if (centavos):
        print('Preco do produto: R$', real.text + ',' + centavos.text)
    else:
        print('Preco do produto: R$', real.text)
        
    print('\n\n')