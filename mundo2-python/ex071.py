
saque = int(input('Que valor voce quer sacar? R$'))

if saque / 50 >= 1:
    
    res = saque // 50
    saque = saque % 50
    print(f'Total de {res} cedulas de R$50')
    

if saque / 20 >= 1:
    res = saque // 20
    saque = saque % 20
    print(f'Total de {res} cedulas de R$20')
    

if saque / 10 >= 1:
    res = saque // 10
    saque = saque % 10
    print(f'Total de {res} cedulas de R$10')

if saque / 5 >= 1:
    res = saque // 5
    saque = saque % 5
    print(f'Total de {res} cedulas de R$5')

if saque / 2 >= 1:
    res = saque // 2
    saque = saque % 2
    print(f'Total de {res} cedulas de R$2')

if saque / 1 >= 1:
    res = saque // 1
    saque = saque % 1
    print(f'Total de {res} cedulas de R$1')

print('FIM')