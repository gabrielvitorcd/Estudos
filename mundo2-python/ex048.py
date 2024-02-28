soma = 0
for c in range(1, 500, 2):
    print(c)
    if c / 3:
        soma += c
    
print('A soma de todos os valores foi {}' .format(soma))