from datetime import date

def voto(nasc):
    idade = date.today().year - nasc
    if idade <= 17:
        print(f'Voce tem {idade} anos, Proibido votar !')
    elif idade >= 18 and idade <= 65:
        print(f'Voce tem {idade} anos, Voto Obrigatorio !')
    elif idade > 65:
        print(f'Voce tem {idade} anos, Voto opicional !')

voto(int(input('Digite sua idade: ')))
