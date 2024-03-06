lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)


    saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if saida in 'N':
        break

print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente sao {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 nao está na lista')