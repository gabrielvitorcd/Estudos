import urllib
import requests

try:
    site = urllib.request.urlopen('https://www.google.com.br/')
except:
    print('PO deu pra conectar nao mano')
else: 
    print('conectei')
    print(site.read())
