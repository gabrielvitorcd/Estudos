while True:
    numero = int(input('Qual numero deseja a tabuada? '))
    if numero < 0:
        break

    for c in range(1,11):
        mult = numero * c
        print(f'{numero} x {c} = {mult}')
        c += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')