valores = []

saida = ''

while True:
    n = int(input('Digite um valor: '))
    
    if n in valores:
        print('Valores Duplicado! Nao vou adicionar')
    else:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    
    saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if saida in 'N':
        break
    
    while saida != 'S':
        saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
print(f'A lista em ordem crescente é: {sorted(valores)}')