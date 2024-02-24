velocidade = float(input('Qual a velocidade que voce estava? '))


if velocidade > 80:
    print('Limite de 80 km/h, Voce foi multado!! ')
    multa = (velocidade - 80) * 7
    print('Sua multa foi de R${:.2f}' .format(multa))
else:
    print('Voce nao foi multado.')