print('-'*20 ,'Aluguel de carros', '-'*20)

km = float(input('Informe o km percorrido: '))
dias = int(input('Informe quantos dias alugou: '))

diaria = dias * 60
kmgasto = 0.15 * km
total = diaria + kmgasto

print('O valor gasto por diaria: R${:.2f}' .format(diaria))
print('O valor gasto por km rodado: R${:.2f}' .format(kmgasto))
print('O valor total gasto: R${:.2f}' .format(total))

