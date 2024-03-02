print('Sequencia de fibonacci')
totaltermo = int(input('Digite quantos termos: '))
termo1 = 0
termo2 = 1

c = totaltermo - 2

print('{} -> {} -> ' .format(termo1,termo2),end='')

while c > 0:
    termo3 = termo2 + termo1
    print(' {} -> ' .format(termo3),end='')
    termo1 = termo2
    termo2 = termo3
    
       
    c-=1

print('FIM')