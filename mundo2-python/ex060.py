fatorial = 1
numero = int(input('Digite um numero para calcular ele fatorial? '))
c = numero
print('Calculando {}! = ' .format(numero), end='')
while c > 0:
    print('{}' .format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial = fatorial * c
    c -= 1
print(' {} ' .format(fatorial) ,end='')