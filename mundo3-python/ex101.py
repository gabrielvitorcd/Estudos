
def voto(nasc):
    from datetime import date #Esse comando dentro da funcao economiza espaco na memoria, visto que só é puxado para isso
    idade = date.today().year - nasc
    if idade <= 17:
        return f'Voce tem {idade} anos, Proibido votar !'
    elif idade >= 18 and idade <= 65:
        return f'Voce tem {idade} anos, Voto Obrigatorio !'
    elif idade > 65:
        return f'Voce tem {idade} anos, Voto opicional !'


idadeusuario = int(input('Digite o ano que voce nasceu: '))
print(voto(idadeusuario))