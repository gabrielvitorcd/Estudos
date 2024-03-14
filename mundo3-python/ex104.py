def leiaInt(msg):
    num = str(input(msg))
    while num.isnumeric() == False:
        print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        num = str(input('Digite um numero: '))
    return int(num)

#PROGRAMA PRINCIPAL
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
