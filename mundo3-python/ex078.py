valores = []
menor = 0
maior = 0
posicaomaior = 0
posicaomenor = 0

for contador in range(0,5):
    valores.append(int(input(f'Digite o valor {contador}: ')))

for chave, valor in enumerate(valores):
        
    if chave == 0:
        maior = valor
        posicaomaior = chave
        menor = valor
        posicaomenor = chave
    else:
        if valor > maior:
            maior = valor
            posicaomaior = chave
        if valor < menor:
            menor = valor
            posicaomenor = chave
           
        

print('-='*30)
print(f'Voce digitou os valores {valores}')
print(f'O maior valor é {maior} na posicao {posicaomaior}')
print(f'O menor valor é {menor} na posicao {posicaomenor}')


    