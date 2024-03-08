galera = []
dado = []
nome = []
maior = 0
menor= 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0:
        maior = dado[1]
        menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
   
    galera.append(dado[:])
    dado.clear()

    saida = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if saida == 'N':
        break



print(f'Ao todo, voce cadastrou {len(galera)} pessoas. ')
print(f'O maior peso foi de {maior}, Peso de ', end='')

for p in galera:
    if p[1] == maior:
        print(f' {p[0]}', end='')
print()
print(f'O menor peso foi de {menor}, Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f' {p[0]}', end='')