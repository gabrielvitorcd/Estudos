dinheiro = int(input('Quanto reais voce deseja converter? R$ '))
valor = float(input('Digite o valor do dolar hoje? '))

dolar = dinheiro / valor


print('Voce consegue comprar US$ {:.2f} dolares' .format(dolar))
