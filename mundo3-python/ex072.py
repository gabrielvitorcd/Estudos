while True:
    numero = (
        "zero", "um", "dois", "três", "quatro", "cinco",
        "seis", "sete", "oito", "nove", "dez", "onze",
        "doze", "treze", "catorze", "quinze", "dezesseis",
        "dezessete", "dezoito", "dezenove", "vinte"
    )


    while True:
        escolha = int(input('Digite um numero de 0 a 20: '))
        if escolha >= 0 and escolha <= 20:
            break
    print(f'Voce digitou o numero {numero[escolha]}')

    saida = ' '
    while saida not in 'SN':
        saida = str(input('Voce quer continuar [S/N]: ')).strip().upper()[0]

    if saida == 'N':
        break