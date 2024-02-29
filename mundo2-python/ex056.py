soma_idade = 0
for c in range(1, 5):
    print('-'*10 , 'Pessoa {}' .format(c),'-'*10 )

    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    soma_idade += idade
    sexo = str(input('Sexo [M/F]: '))


print('A media de idade do grupo é de {} anos'.format(soma_idade / c))
print('O homem mais velho tem {} anos e se chama {}')
print('Ao todo sao {} mulheres com menos de {} anos')