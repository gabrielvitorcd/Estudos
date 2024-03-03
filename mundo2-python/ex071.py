
saque = int(input('Que valor voce quer sacar? R$'))

if saque / 50 >= 1:
    while True:
        res = saque // 50
        saque = saque % 50
        print(f'Total de {res} cedulas de R$50')
        break

if saque / 20 >= 1:
    while True:
        res = saque // 20
        saque = saque % 20
        print(f'Total de {res} cedulas de R$20')
        break

if saque / 10 >= 1:
    while True:
        res = saque // 10
        saque = saque % 10
        print(f'Total de {res} cedulas de R$10')
        break

if saque / 5 >= 1:
    while True:
        res = saque // 5
        saque = saque % 5
        print(f'Total de {res} cedulas de R$5')
        break

if saque / 2 >= 1:
    while True:
        res = saque // 2
        saque = saque % 2
        print(f'Total de {res} cedulas de R$2')
        break

if saque / 1 >= 1:
    while True:
        res = saque // 1
        saque = saque % 1
        print(f'Total de {res} cedulas de R$1')
        break

print('FIM')