num = str(input('Digite um numero 0 até 9999:  '))

if (len(num) > 3) and (len(num) <= 4):
    print('Unidade: {}' .format(num[3:]))
    print('Dezena: {}' .format(num[2:3]))
    print('Centena: {}' .format(num[1:2]))
    print('Milhar: {}' .format(num[:1]))

elif (len(num) > 2) and (len(num) <= 3):
    print('Unidade: {}'.format(num[2:]))
    print('Dezena: {}'.format(num[1:2]))
    print('Centena: {}'.format(num[:1]))

elif (len(num) > 1) and (len(num) <= 2):
    print('Unidade: {}'.format(num[1:]))
    print('Dezena: {}'.format(num[:1]))

elif (len(num) >= 1) and (len(num) < 2):
    print('Unidade: {}'.format(num[:]))

else:
    print('numero invalido, Digite outro numero')