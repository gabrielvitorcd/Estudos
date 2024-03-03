pessoas18 = 0
homens = 0
mulheresnovas = 0



while True:
    idade = int(input('IDADE: '))

    sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]

    saida = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

    if idade >= 18:
        pessoas18 += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade <= 20:
        mulheresnovas += 1

    if saida in 'N':
        break

print(f'Total de pessoas mais de 18 anos: {pessoas18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheresnovas} com menos de 20 anos')