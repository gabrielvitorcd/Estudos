cadastro = dict()
pessoa = list()
soma = 0
soma2 = 0
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
print(f'Ao todo temos {len(pessoa)} pessoas cadastradas')
print(f'A media de idade é de {soma/len(pessoa)}')
for c in pessoa:   #assisit aula do for e estudar
    print(pessoa[c]['idade'])

print(soma2)
print(cadastro)