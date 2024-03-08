galera = []
dado = []
totpessoas = 0
maiorpeso = [0]
nome = ['']
maior = 0
menor= 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    totpessoas += 1
    galera.append(dado[:])
    dado.clear()

    
    for p in galera:
        if p[1] >maiorpeso[0]:
            maiorpeso.insert(0, p[1])
            maiorpeso.pop()
            nome.insert(0 ,p[0])
            nome.pop

    
    saida = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if saida == 'N':
        break



print(f'Ao todo, voce cadastrou {totpessoas} pessoas. ')
print(f'O maior peso foi de {maiorpeso} Peso de {nome}')