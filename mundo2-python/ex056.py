soma_idade = 0
maioridademasc = 0
nomevelho = ''
mulheresnovas = 0

for pessoa in range(1, 5):
    print('-'*10, 'Pessoa {}' .format(pessoa), '-'*10)

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    soma_idade += idade
    sexo = str(input('Sexo [M/F]: ')).strip()

    if pessoa == 1 and sexo in 'Mm':
        maioridademasc = idade
        nomevelho = nome
    else:
        if idade > maioridademasc and sexo in 'Mm':
            maioridademasc = idade
            nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        mulheresnovas += 1

print('A media de idade do grupo é de {} anos'.format(soma_idade / pessoa))
print('O homem mais velho tem {} anos e se chama {}' .format(
    maioridademasc, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos' .format(mulheresnovas))
