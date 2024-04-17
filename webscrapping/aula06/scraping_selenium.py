from selenium import webdriver
from time import sleep

navegador = webdriver.Firefox()

navegador.get('https://www.google.com/')

sleep(3)

busca = navegador.find_element(by='tag name',value='textarea')

busca.send_keys('bbb24')
