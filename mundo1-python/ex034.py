salario = float(input('Escreva seu salario: '))

if salario > 1250:
    aumento = salario + (salario * 0.10)
    print('O seu salario aumentou 10%. Foi de R${:.2f} PARA R${:.2f}' .format(salario, aumento))
else:
    aumento = salario + (salario * 0.15)
    print('O seu salario aumentou 15%. Foi de R${:.2f} PARA R${:.2f}' .format(salario, aumento))