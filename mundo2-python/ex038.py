print('='*30, 'Comparador de Numeros', '='*30)

num1 = int(input('Insira o numero 1: '))
num2 = int(input('Insira o numero 2: '))

if num1 > num2:
    print('O numero 1: {} é maior que o Numero 2: {}' .format(num1, num2))
elif num2 > num1:
    print('O numero 2: {} é maior que o Numero 1: {}' .format(num2, num1))
else:
    print('Os dois valores são iguais')
