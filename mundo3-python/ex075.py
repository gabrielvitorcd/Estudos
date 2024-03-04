pares = 0
num = (int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),)
   
for n in num:
    if n % 2 == 0:
        pares+=1

print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posicao')
else:
    print('Nenhum valor 3 foi digitado')
print(f'Os valores pares digitados foram {pares}')