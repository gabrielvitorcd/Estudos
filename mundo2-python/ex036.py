print('='*20, 'Aprovador de Emprestimos', '='*20)

valor_casa = float(input('Qual valor da casa? '))
salario = float(input('Qual valor do seu salario? '))
meses = int(input('Em quantos meses quer financiar? '))

parcela = valor_casa / meses

if parcela > salario * 0.3:
    print('Emprestimo \033[4;31mNegado')

else:
    print('Emprestimo \033[4;32mAprovado')