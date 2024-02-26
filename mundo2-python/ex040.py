print('='*30, 'PROGRAMA APROVOÇÃO ESCOLAR', '='*30)

nota1 = float(input('Insira nota 1: '))
nota2 = float(input('Insira nota 2: '))

media = (nota1 + nota2) / 2
print('Sua media foi: {}' .format(media))

if media < 5.0:
    print('Reprovado')
elif media >= 5 and media < 7:
    print('Recuperação')
else:
    print('Aprovado')
