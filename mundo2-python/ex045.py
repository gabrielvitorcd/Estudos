import time
from random import randint
print('='*30, 'JOGO JOKENPO', '='*30)


usuario = int(input('Selecione:\n1- Pedra\n2- Papel\n3- Tesoura\n'))
maquina = randint(1, 3)


print('Processando...')
time.sleep(1)

if usuario == 1:
    print('Voce1: PEDRA')
elif usuario == 2:
    print('Voce: PAPEL')
elif usuario == 3:
    print('Voce: TESOURA')

if maquina == 1:
    print('O Pc: PEDRA')
elif maquina == 2:
    print('O Pc: PAPEL')
elif maquina == 3:
    print('O Pc: TESOURA')

if usuario == maquina:
    print('Empate!')
elif (usuario == 1 and maquina == 3) or (usuario == 2 and maquina == 1) or (usuario == 3 and maquina == 2):
    print('Você ganhou!')
else:
    print('Você perdeu!')
