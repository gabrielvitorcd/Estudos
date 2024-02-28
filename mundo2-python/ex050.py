soma = 0

for c in range(1, 7):
    numreal = int(input('Digite um numero: '))
    
    if numreal % 2 == 0:
       soma += numreal
    
    elif numreal % 2 == 1:
        print('Valor Considerado')        
       
print('A soma de todos os pares {}' .format(soma))
        
