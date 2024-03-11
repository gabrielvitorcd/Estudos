from datetime import date

pessoa = {}

pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - ano
pessoa['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
print('-='*30)
if pessoa['ctps'] == 0:
    for k, v in pessoa.items():
        print(f'- {k} tem o valor {v}')
else:
    pessoa['contratacao'] = int(input('Ano de contratacao: '))
    pessoa['salario'] = float(input('Salario: R$'))
    pessoa['aposentadoria'] = pessoa['contratacao'] + 35 - ano
    for k, v in pessoa.items():
        print(f'- {k} tem o valor {v}')
