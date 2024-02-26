from datetime import date

anonascimento = int(input('Insira o ano do seu nascimeto: '))
idade = date.today().year - anonascimento

print('A sua idade é: {} Anos' .format(idade))

if idade <= 9:
    print('Até 9 anos: Mirim')
elif idade > 9 and idade <= 14:
    print('Até 14 anos: Infantil')
elif idade > 14 and idade <= 19:
    print('Até 19 anos: Junior')
elif idade > 19 and idade <= 20:
    print('Até 20 anos: Senior')
else:
    print('Acima de 20 anos: Master')
