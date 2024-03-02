c = 0
contador = 0
total = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    contador += 1
    total += num 
    num = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} números e a soma entre eles foi {}' .format(contador,total))