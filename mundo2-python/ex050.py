soma = 0
contador = 0

for c in range(1, 7):
    numreal = int(input('Digite {} numero: ' .format(c)))
    
    if numreal % 2 == 0:
       soma += numreal
       contador = contador + 1       
       
print('Voce informou {} numeros pares e a soma foi {}' .format(contador,soma))
        
