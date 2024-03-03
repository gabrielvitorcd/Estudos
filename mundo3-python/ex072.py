numero = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez", "onze",
    "doze", "treze", "catorze", "quinze", "dezesseis",
    "dezessete", "dezoito", "dezenove", "vinte"
)

escolha = int(input('Digite um numero de 0 a 20: '))

if escolha < 0 or escolha > 20:
    while True:
        escolha = int(input('Digitacao ERRADA, TENTE NOVAMENTE. Digite um numero de 0 a 20: '))
        if escolha >= 0 and escolha <= 20:
            break

print(f'Voce digitou o numero {numero[escolha]}')