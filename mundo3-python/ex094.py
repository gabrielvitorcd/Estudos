cadastro = dict()
pessoa = list()

while True:

    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while cadastro['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    cadastro['idade'] = int(input('Idade: '))
    
    pessoa.append(cadastro.copy())
    cadastro.clear()




    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('ERRO! Por favor, digite apenas M ou F')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(pessoa)
print(cadastro)