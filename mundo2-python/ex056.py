# Inicialização das variáveis para armazenar a soma das idades, a maior idade masculina,
# o nome do homem mais velho e o número de mulheres com menos de 20 anos.
soma_idade = 0
maioridademasc = 0
nomevelho = ''
mulheresnovas = 0

# Loop para iterar sobre as 4 pessoas
for pessoa in range(1, 5):
    # Imprime um cabeçalho indicando a pessoa atual
    print('-'*10, 'Pessoa {}' .format(pessoa), '-'*10)

    # Solicita e armazena o nome, idade e sexo da pessoa
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    soma_idade += idade  # Adiciona a idade atual à soma total das idades
    sexo = str(input('Sexo [M/F]: ')).strip()

    # Verifica se a pessoa atual é a primeira e se é um homem
    if pessoa == 1 and sexo in 'Mm':
        maioridademasc = idade  # Se sim, define a maioridade masculina como a idade atual
        nomevelho = nome  # e o nome do homem mais velho como o nome atual
    else:
        # Caso contrário, verifica se a idade atual é maior que a maior idade masculina até agora
        # e se a pessoa atual é um homem
        if idade > maioridademasc and sexo in 'Mm':
            # Se sim, atualiza a maioridade masculina e o nome do homem mais velho
            maioridademasc = idade

    # Verifica se a pessoa atual é uma mulher com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        mulheresnovas += 1  # Se sim, incrementa o contador de mulheres com menos de 20 anos

# Após o loop, exibe as informações calculadas
print('A media de idade do grupo é de {} anos'.format(soma_idade / pessoa))
print('O homem mais velho tem {} anos e se chama {}' .format(
    maioridademasc, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos' .format(mulheresnovas))
