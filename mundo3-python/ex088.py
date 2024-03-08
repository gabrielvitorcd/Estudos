from random import randint
import time

jogadas = int(input('Quantos jogos voce quer que eu sorteie? '))

for c in range(1,jogadas+1):
    jogo = [[randint(1,60)],[randint(1,60)],[randint(1,60)],[randint(1,60)],[randint(1,60)],[randint(1,60)]]
    print(f'Jogo {c}: {jogo}')