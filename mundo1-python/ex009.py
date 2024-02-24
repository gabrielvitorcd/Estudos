print('-' * 40)

n1 = int(input('Digite um numero '))
contador = 1

print('Tabuada de {:=^12}' .format(n1))

while(contador <= 10):
    print('Tabuada de {} x {:2} = {:2}' .format(n1, contador, n1 * contador)  )
    contador = contador + 1

else:
    print('-' * 40)

