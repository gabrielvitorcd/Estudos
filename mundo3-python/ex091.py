from time import sleep
from random import randint
from operator import itemgetter


valores = dict()

for c in range(1,5):
    num = randint(1,6)
    valores[f'jogador{c}'] = num
ranking = list()
print('Os valores sorteados:\n')
for k, v in valores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(valores.items(), key=itemgetter(1),reverse=True) # esse comando converte o indice 1 do dicionario em lista e ordena em ordem decrescente
print('-='*30)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)