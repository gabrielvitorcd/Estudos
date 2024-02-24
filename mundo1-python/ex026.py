frase = str(input('Insira uma frase: ')).strip().lower()

print('A letras "A" aparece {} vezes na frase.' .format(frase.count('a')))
print('Em que posicao aparece na primeira vez: {}' .format(frase.find('a') + 1))
print('Em que posicao aparece na ultima vez: {}' .format(frase.rfind('a') + 1))
