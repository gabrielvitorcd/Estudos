c = 1
contador = 0
total = 0

while c != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    contador += 1
    total += num 
    c = num

print('Voce digitou {} números e a soma entre eles foi {}' .format(contador - 1,total - 999))