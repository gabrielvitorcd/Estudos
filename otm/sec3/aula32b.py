hora = input('Digite a hora atual: ')

if hora.isnumeric():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora > 17 and hora <= 23:
        print('Boa noite')
    else:
        print('Digite um hora valida')
else:
    print('Voce nao digitou um numero')