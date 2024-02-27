print('='*30, 'CALCULADORA DE IMC', '='*30)

altura = float(input('Insira sua altura: '))
peso = float(input('Insira seu peso: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é: {:.1f}- ABAIXO DO PESO !!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é: {:.1f}- PESO IDEAL!!' .format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é: {:.1f}- SOBREPESO' .format(imc))
else:
    print('Seu IMC é: {:.1f}- OBESIDADE MORBIDA' .format(imc))
