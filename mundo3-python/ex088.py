from random import randint
import time
lista = []
jogos = []
jogada = int(input('Quantos numeros quer que eu sorteie? '))
tot = 1

while tot <= jogada:
    contador = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

for i,c in enumerate(jogos,1):
    print(f'Jogo {i}: {c}')


