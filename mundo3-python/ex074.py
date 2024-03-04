from random import randint

sorteio = (randint(0,10), randint(0,10), randint(0,10), randint(0,10),randint(0,10))

print('Os valores sorteados foram: ', end='')

for c in sorteio:
    print(f'{c} ', end='')

print('\nO maior valor foi {}'.format(sorted(sorteio)[-1]))
print('O menor valor foi {}'.format(sorted(sorteio)[0]))