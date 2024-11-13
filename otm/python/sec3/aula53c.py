"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


for indice, nome in enumerate(lista):
    print(indice,'/',nome,lista[indice])

print('-'*30)
for item in enumerate(lista):
    print(item)
    indice, nome = item         #Desempacotamento da tupla criada dentro do FOR
    print(indice,'/',nome)

print('-'*30)
for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:   #FOR que ler os valores dentro da tupla_enumerada
        print(f'\t{valor}')