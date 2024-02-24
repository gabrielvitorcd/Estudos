num = int(input('Insira um numero'))

milhar = num // 1000 % 10
centena = num // 100 % 10
dezena = num // 10 % 10
unidade = num // 1 % 10


if num > 9999:
    print('O numero é invalido')

elif num <= 9999:
    print('Unidade: {}' .format(unidade))
    print('Dezena: {}' .format(dezena))
    print('Centena: {}' .format(centena))
    print('Milhar: {}' .format(milhar))
