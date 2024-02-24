print('='*10,'TABELA DE AUMENTO', '='*10)

salario = float(input('Insira quanto recebe: R$ '))
aumento = salario * 15/100
bruto = salario + aumento

print('Valor do salario atual: R$ {}' .format(salario))
print('Valor do aumento: R$ {:.1f}' .format(aumento))
print('Valor do seu salario com aumento: R$ {:.1f}' .format(bruto))