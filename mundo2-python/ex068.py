from random import randint
print('JOGO DE IMPAR OU PAR')

vitorias = 0
while True:
    computador = randint(1, 10)
    usuario = int(input('Diga um valor: '))
    
    escolha = ' '         
    while escolha not in 'PI':  #Validacao para o usuario digitar somente p ou i
        escolha = str(input('Par ou Impar? [P/I]')).strip().upper()[0]

    somatotal=computador + usuario

    if somatotal % 2 == 1:
        deu = 'IMPAR'
    else:
        deu = 'PAR'

    if escolha == 'P' and somatotal % 2 == 0:
        resultado = 'VENCEU'
    elif escolha == 'I' and somatotal % 2 == 1:
        resultado = 'VENCEU'
    else:
        resultado = 'PERDEU'
        break
    vitorias += 1
   
    print(f'Voce jogou {usuario} e o computador {computador}. Total de {somatotal} deu {deu} ')
   

print(f'Voce jogou {usuario} e o computador {computador}. Total de {somatotal} deu {deu} ')
print('='*35)
print(f'Voce {resultado}')
print('='*35)
print(f'Gamer Over! Voce venceu {vitorias} vezes\n')


