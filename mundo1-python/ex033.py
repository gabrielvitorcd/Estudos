num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
num3 = int(input('Numero 3: '))

lista = [num1, num2, num3]
lista.sort()
#.sort() -> Ordena a lista em ordem crescente

print('O menor numero é: {}' .format(lista[0]))
print('O maior numero é: {}' .format(lista[-1]))
