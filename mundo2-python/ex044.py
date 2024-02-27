print('='*30, 'PROGRAMA QUE ANALISA A FORMA DE PAGAMENTO E CALCULA O VALOR FINAL', '='*30)

valor = float(input('Insira o valor do produto: '))

print('Qual forma de pagamento:\n1- Avista Dinheiro ou Cheque\n2- Avista Cartão\n3- Parcelado 2 vezes\n4- Parcelado 3 ou mais')

formapagamento = int(input('Insira a sua forma de Pagamento: '))

if formapagamento == 1:
    precofinal = valor - (valor*0.1)
    print('Voce ganhou 10% de desconto: R${:.2f}' .format(precofinal))
elif formapagamento == 2:
    precofinal = valor - (valor*0.05)
    print('Voce ganhou 5% de desconto: R${:.2f}' .format(precofinal))
elif formapagamento == 3:
    print('Voce vai pagar o valor normal do produto: R${:.2f}' .format(valor))
elif formapagamento == 4:
    precofinal = valor + (valor*0.2)
    print('Voce vai pagar 20% de juros: R${:.2f}' .format(precofinal))
else:
    print('Insira uma opção valida')
