print('='*30,'Conversor de Base Numerica','='*30)

numero = int(input('Qual numero voce deseja converter: '))
base = int(input('Qual a base de conversão?\n1 Para binario\n2 Para Octal\n3 para hexadecimal\n'))
contador = 1
calculo1 = numero / 2  

if base==1:
    print('binario')
    while numero / 2 == 0 or numero / 2 == 1: 
        print(calculo1 % 2)
        contador + 1
elif base==2:
    print('octal')
elif base==3:
    print('hexadecimal')
else:
    print('Insira um numero de 1 a 3')