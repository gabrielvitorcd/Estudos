galera = []
dado = []
totpessoas = 0
maiorpeso = [[0]]
nome = []
maior = 0
menor= 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    totpessoas += 1
    galera.append(dado[:])
    dado.clear()

 
            

    
    saida = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if saida == 'N':
        break



print(f'Ao todo, voce cadastrou {totpessoas} pessoas. ')
   
for p in galera:
    if p[1] >= maior:
        maior = p[1]
        nome.append(p[0])
        
print(f'O maior peso foi de {maior}, Peso de {nome}')