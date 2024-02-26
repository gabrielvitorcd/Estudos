from datetime import date
print('='*30, 'PROGRAMA DE ALISTAMENTO MILITAR', '='*30)


anonascimento = int(input('Informe o ano que voce nasceu? '))
idade = date.today().year - anonascimento
faltaprazo = 18 - idade
passouprazo = idade - 18

if idade < 18:
    print('Voce ainda vai se alistar. Falta: {} anos para se alistar' .format(faltaprazo))

elif idade == 18:
    print('Está na hora de se alistar.')
else:

    print('Passou seu tempo de alistamento.  Voce excedeu: {} anos do seu alistamento' .format(passouprazo))
