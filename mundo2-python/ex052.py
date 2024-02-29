numero = int(input('Digite um numero: '))
contador = 0

for c in range(1, numero+1):
   
    if numero % c == 0:
        print('\033[33m', end= '')
        contador = contador + 1
    else:
        print('\033[31m', end= '')
    
    print('{} ' .format(c), end= '')

print('\n\033[mO numero {} foi divisivel {} vezes ' .format(numero, contador))

if contador == 2:
    print('É um numero PRIMO')
else:
    print('Nao é PRIMO')