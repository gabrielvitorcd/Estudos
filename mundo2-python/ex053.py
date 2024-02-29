frase = str(input('Digite uma frase: '))
remocao = ''.join(frase.split()).upper()

print('A frase normal fica: {}' .format(remocao))
print('A frase invertida fica: {}' .format(remocao[::-1]))

if remocao == remocao[::-1]:
    print('É um palíndromos')
else:
    print('Nao é um palíndromos')


