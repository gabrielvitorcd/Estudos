print('Desafio tabuada')
numero = int(input('Insira o numero que deseja calcular: '))

for c in range(1,11):
    tabuada = numero * c
    print('{} x {} = {}' .format(c, numero, tabuada))