import time

num1 = float(input('Medida 1: '))
num2 = float(input('Medida 2: '))
num3 = float(input('Medida 3: '))

print('Processando...')
time.sleep(2)

if num1 + num2 > num3 and num2 + num3 > num1 and num1 + num3 > num2:
    print('É possivel fazer um triangulo')
    if num1 == num2 == num3:
        print('É um Triangulo Equilatero: Todos os lados iguais')
    elif num1 == num2 or num2 == num3 or num1 == num3:
        print('É um Triangulo isoceles: Dois lados iguais')
    else:
        print('É um Triangulo Escaleno: Todos os lados diferentes')


else:
    print('Nao é possivel o triangulo')
