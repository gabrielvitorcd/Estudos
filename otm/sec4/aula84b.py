# List comprehension em Python
# List comprehension é uma forma rapida para criar listas
# a partir de iteraveis

print(list(range(10)))

lista_2 = []

for numero in range(10):
    lista_2.append(numero)

print(lista_2)


lista_3 = [
    numero * 2      #as condicoes vem antes do for
    for numero in range(10)
]

print(lista_3)


# Mapeamento de dados em list comprehension
# produtos = [
#   {'nome':'p1', 'preco': 20, },
# ]