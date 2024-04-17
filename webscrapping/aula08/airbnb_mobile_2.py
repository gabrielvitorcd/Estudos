from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd


lugar_usuario = input('Digite um lugar para pesquisar: ')

navegador = webdriver.Firefox()
navegador.set_window_size(400,800)
navegador.get('https://www.airbnb.com.br/')
sleep(4)

# abrir barra de pesquisa
open_buscar = navegador.find_element(by='tag name',value='button')
open_buscar.click()
sleep(2)

#pesquisa local
pesquisar_local = navegador.find_elements(by='tag name',value='button')[86]
pesquisar_local.click()

#buscar lugar
input_place = navegador.find_element(by='id',value='/homes-where-input')
input_place.send_keys(lugar_usuario)
input_place.submit()


#data selection
selecionar_ida = navegador.find_elements(by='tag name',value='td')[5]  #dia do mes
selecionar_ida.click()

selecionar_volta = navegador.find_elements(by='tag name',value='td')[7]  #dia do mes
selecionar_volta.click()


# selecionar proximo
data_proximo = navegador.find_elements(by='tag name',value='button')[-4]
data_proximo.click()

#quantidade de pessoa clicando
quantidade_clic = navegador.find_elements(by='tag name',value='button')[-10]
quantidade_clic.click()
quantidade_clic.click()


# selecionar proximo 2 
sel_proxim = navegador.find_elements(by='tag name',value='span')[-2]
sel_proxim.click()


# OK tela cockies 
sel_ok = navegador.find_elements(by='tag name',value='button')[-1]
sel_ok.click()
sleep(5)

page_content = navegador.page_source

site = BeautifulSoup(navegador.page_source, 'html.parser')

dados_hospedagens = []

hospedagens = site.find_all('div', attrs={'itemprop': 'itemListElement'})

for hospedagem in hospedagens:

   # print(hospedagem.prettify())

    hospedagem_descricao = hospedagem.find('meta', attrs={'itemprop':'name'})['content']
    hospedagem_url = hospedagem.find('meta', attrs={'itemprop': 'url'})['content']
    preco_noite = hospedagem.find_all('span')[-11].text
    preco_total = hospedagem.find_all('span')[-7].text[:14]
    

    print(f'Descricao: {hospedagem_descricao}')
    print(f'URL: {hospedagem_url}')
    print(f'Preco por noite: {preco_noite}')
    print(f'Preco TOTAL: {preco_total}')

    print()

    dados_hospedagens.append([hospedagem_descricao,hospedagem_url,preco_noite,preco_total])

dados_airbnb = pd.DataFrame(dados_hospedagens, columns=['Titulo', 'URL', 'Preco por noite','Preco total'])

dados_airbnb.to_excel('dados_airbnb.xlsx', index=False)
