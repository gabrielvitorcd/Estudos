from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

navegador = webdriver.Firefox()
#navegador.set_window_size(400,800)
navegador.get('https://www.airbnb.com')
sleep(5)

input_place = navegador.find_element(by='id',value='bigsearch-query-location-input')
input_place.send_keys('rio de janeiro')
input_place.submit()
sleep(5)

#abrir opcoes
opcoes_stay = navegador.find_element(by='class name', value='f16sug5q')
opcoes_stay.click()
sleep(2)

#selecionar ida
selecionar_ida = navegador.find_element(by='class name', value='p1m42al0')
selecionar_ida.click()
sleep(2)

#selecionar sexta
selecionar_sexta = navegador.find_element(by='class name',value='_1aj90y58.notranslate')
selecionar_sexta.click()
sleep(2)


#selecionar segunda
selecionar_segunda = navegador.find_element(by='class name',value='_sl5yz7r')
selecionar_segunda.click()
sleep(2)


#buscar 
selecionar_search = navegador.find_element(by='class name',value='bhtghtc')
selecionar_search.click()

sleep(5)

#conteudo da busca
page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

print(site.prettify())




