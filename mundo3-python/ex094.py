cadastro = dict()
pessoa = list()
soma = 0
while True:

    cadastro['nome'] = str(input('Nome: '))

    cadastro['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while cadastro['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']

    pessoa.append(cadastro.copy())
    cadastro.clear()

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('ERRO! Por favor, digite apenas M ou F')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
media = soma/len(pessoa)

print(f'A) Ao todo temos {len(pessoa)} pessoas cadastradas')
print(f'B) A media de idade é de {media:.1f}')
print('C) As mulheres cadastradas foram ', end='')
for c in pessoa:
    if c['sexo'] in 'F':
        print(c['nome'], end=' ')
print()
print('D) Listas das pessoas que estao acima da media: ')
for l in pessoa:
    if l['idade'] > media:
        for k, v in l.items():
            print(f'{k} = {v}; ', end='')
        print()
print('Encerrado!')
