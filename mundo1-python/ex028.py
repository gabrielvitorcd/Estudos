from random import randint
from time import sleep

numvc = int(input('Insira um numero: '))
nummaquina = randint(0,5)
print('Processando... ')
sleep(3)

if (numvc >= 0) and (numvc <= 5):
    if numvc == nummaquina:
        print('Voce Acertou!!! PARABENS. Eu pensei no numero {}' .format(nummaquina))
    else:
        print('Voce ERROU, Eu pensei no numero {}' .format(nummaquina))
else:
    print('Numero Invalido, Insiro um numero de 0 a 5.')