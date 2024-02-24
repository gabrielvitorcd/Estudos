distancia = int(input('Qual foi a distancia em km/h percorrida: '))

if distancia <= 200:
    calculo = distancia * 0.5
    print('Sua passsagem custara R${:.2f}' .format(calculo))
else:
    calculo = distancia * 0.45
    print('Suua passagem custara R${:.2f}' .format(calculo))