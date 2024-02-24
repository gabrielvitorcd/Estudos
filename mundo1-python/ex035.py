import time

num1 = float(input('Medida 1: '))
num2 = float(input('Medida 2: '))
num3 = float(input('Medida 3: '))

print('Processando...')
time.sleep(2)

if num1 + num2 > num3 and num2 + num3 > num1 and num1 + num3 > num2:
    print('É possivel fazer um triangulo')
else:
    print('Nao é possivel o triangulo')