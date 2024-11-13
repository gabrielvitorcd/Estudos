#Jogo do GV
print('jogo do gv'.title(),
      '\nTente adivinhar qual palavra eu pensei... rs')
import os

palavra_maquina = 'Quarto'.lower()
letras_acertadas = ''
numeros_tentivas = 0

while True:
    letra_usuario = input('Digite uma letra que eu te digo se acertou: ').lower()
    if len(letra_usuario) > 1 or len(letra_usuario) == False:
        os.system('clear')
        print('Faça a digitação correta! Digite apenas uma letra.')
        continue
    numeros_tentivas += 1
    if letra_usuario in palavra_maquina:
        letras_acertadas += letra_usuario
        os.system('clear')
        print('Voce acertou uma letra')
    else:
        os.system('clear')
        print('Desculpe, Voce não acertou a letra')
    print(f'Aqui todas as letras que acertou: "{letras_acertadas}"')
    
    palavra_usuario = input('Qual seu papite sobre qual palavra pensei... ')
    

    if palavra_usuario == palavra_maquina:
        break
    else:
        os.system('clear')
        print('Tenta mais uma vez!')


os.system('clear')
print('Parabens você acertou!!!')
print(f'Voce Tentou por {numeros_tentivas} vezes.')