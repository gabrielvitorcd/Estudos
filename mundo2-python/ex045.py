from random import randint
import time

itens  = ('Pedra', 'Papel' , 'Tesoura')
maquina = randint (0, 2)
usuario = int(input('''
[ 0 ]- Pedra
[ 1 ]- Papel
[ 2 ]- Tesoura
Qual a sua jogada? 
'''))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('-=' * 15)

print('O computador escolheu: {}' .format(itens[maquina]))
print('Voce escolheu: {}' .format(itens[usuario]))

print('-=' * 15)

if usuario == maquina:
    print('Empate!')
elif (usuario == 0 and maquina == 2) or (usuario == 2 and maquina == 1) or (usuario == 1 and maquina == 0):
    print('VOCE GANHOU DA MAQUINA!')
else:
    print('A MAQUINA GANHOU VOCE!')