import requests

url = 'https://www.google.com.br/'

response = requests.get(url)


if response.status_code == 200:
    print('conectei ')
else:
    print('PO deu pra conectar nao mano')
