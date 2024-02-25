print('='*30,'Conversor de Base Numerica','='*30)

numero = int(input('Qual numero voce deseja converter: '))
base = int(input('Qual a base de conversão?\n1 Para binario\n2 Para Octal\n3 para hexadecimal\n'))

if base==1:
    numero_binario = bin(numero)[2:]
    print('O numero BINARIO é: {}' .format(numero_binario))

elif base==2:
    numero_octa = oct(numero)[2:]
    print('O numero OCTAL é: {}' .format(numero_octa))
elif base==3:
    numero_hexa = hex(numero)[2:]
    print('O numero HEXADECIMAL é: {}' .format(numero_hexa.upper()))
    
else:
    print('Insira um numero de 1 a 3')