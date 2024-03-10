import time
import random

valores = dict()

for c in range(1,5):
    num = random.randint(1,6)
    valores[f'jogador{c}'] = num

print('Os valores sorteados:\n')
for k, v in valores.items():
    print(f'O {k} tirou: {v}')