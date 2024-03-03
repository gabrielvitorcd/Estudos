total = 0
altovalor = 0
menorvalor = 0
nomeproduto = ''
voltas = 0

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preco: R$'))
    total += preco
    saida = str(input('Voce quer continuar [S/N]')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Voce quer continuar [S/N]')).strip().upper()[0]

    if preco >= 1000:
        altovalor += 1
    
    
    if voltas == 1:
        menorvalor = preco
        nomeproduto = nome 
    else:
        if preco < menorvalor:
            menorvalor = preco 
            nomeproduto = nome 
         
    voltas+=1
    if saida == 'N':
        break

print('-'*20,'FIM DO PROGRAMA','-'*20)
print('O total da compra foi R${:.2f}' .format(total))
print('Temos {} produtos custando mais de R$1000.00' .format(altovalor))
print('O produto mais barato foi {} que custa R${:.2f}'.format(nomeproduto,menorvalor))
