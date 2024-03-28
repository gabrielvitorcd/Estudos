"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

print(lista_enumerada) #localização do iterador na memoria

for item in lista_enumerada:
    print(item)