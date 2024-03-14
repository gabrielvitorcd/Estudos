def leiaInt(msg):
    num = str(input(msg))
    while num.isnumeric() == False:
        print('ERRO!')
        num = str(input('Digite um numero: '))
    return int(num)

n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
