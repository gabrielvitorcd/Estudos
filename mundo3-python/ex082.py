completa = []
pares = []
impares = []
while True:
    num = int(input('Digite um valor: '))
    completa.append(num)

    if num % 2 == 0:
        pares.append(num)
    if num % 2 == 1:
        impares.append(num)
               
    
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'A lista completa é {completa}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')