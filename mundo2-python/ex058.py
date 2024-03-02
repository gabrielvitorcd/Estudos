from random import randint
computador = randint(1,10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10')
print('Sera que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1

    if jogador == computador:
        acertou = True
    
    else:
        if jogador > computador:
            print('Menos... Tente Novamente')
        elif jogador < computador:
            print('Mais... Tente Novamente')

print('Acertou !!!!')
print('O numero que a maquina escolheu foi: {}' .format(computador))
print('Total de tentativas {}' .format(palpites))
