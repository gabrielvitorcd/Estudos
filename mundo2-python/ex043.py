print('='*30, 'CALCULADORA DE IMC', '='*30)

altura = float(input('Insira sua altura: '))
peso = float(input('Insira seu peso: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é: {:.1f}- ABAIXO DO PESO !!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é: {:.1f}- PESO IDEAL!!' .format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é: {:.1f}- SOBREPESO' .format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {}- OBESIDADE' .format(imc))
else:
    print('Seu IMC é: {:.1f}- OBESIDADE MORBIDA' .format(imc))
