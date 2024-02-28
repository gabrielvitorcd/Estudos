print('{:=^40}' .format('LOJAS GV'))

valor = float(input('Insira o valor do produto: '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao
''')

formapagamento = int(input('Insira a sua forma de Pagamento: '))

if formapagamento == 1:
    precofinal = valor - (valor*0.1)
    print('Voce ganhou 10% de desconto: R${:.2f}' .format(precofinal))
elif formapagamento == 2:
    precofinal = valor - (valor*0.05)
    print('Voce ganhou 5% de desconto: R${:.2f}' .format(precofinal))
elif formapagamento == 3:
    print('Voce vai pagar o valor normal do produto: R${:.2f}' .format(valor))
    print('Parcelado em 2x: R${:.2f}' .format(valor / 2)) 
elif formapagamento == 4:
    precofinal = valor + (valor*0.2)
    parcela = int(input('Insira Quantas Parcelas: '))
    print('Voce vai pagar 20% de juros: R${:.2f}' .format(precofinal))
    print('Voce parcelou em {}x: R${:.2f}' .format(parcela, precofinal / parcela))
else:
    print('Insira uma opção valida')
