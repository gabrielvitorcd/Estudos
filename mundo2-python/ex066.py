soma = 0
cont = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999: # O break antes das somas, desconsidera o valor 999
        break
    cont += 1
    soma += num

print(f'A soma dos  {cont} valores foi {soma}')