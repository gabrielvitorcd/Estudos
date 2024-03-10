aluno = {}

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Media: '))
aluno['Situacao'] = ''

if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')