from datetime import date


ano = int(input('Insira o ano que deseja calcular: '))
#considera ano bisexto: ano / 4 ou ano terminado em 00 disivel por 400
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('O ano {}, É BISEXTO' .format(ano))
else:
    print('O ano {}, NAO É BISEXTO' .format(ano))

