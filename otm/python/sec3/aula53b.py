"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista,start=15))

print(lista_enumerada)

#for item in enumerate(lista):
#    print(item)