from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


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
input_place.send_keys('buzios')
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

print(site.prettify())

