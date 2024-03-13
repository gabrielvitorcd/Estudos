from random import randint
from time import sleep

num = list()
def sorteando(val):
   
    for c in range(1,val+1):
        num.append(randint(1,10))
    print(f'Sorteando {len(num)} valores da lista: ', end = '')
    for c in num:
        print(c, end=' ',flush=True)
        sleep(0.3)
    print('PRONTO!')
def somando():
    somapar = 0
    for c in num:
        if c % 2 == 0:
            somapar += c
    print(f'Somando os valores pares de {num}, temos {somapar}')

sorteando(5)
somando()