valores = []
menor = 0
maior = 0
for contador in range(0,5):
    valores.append(int(input(f'Digite o valor {contador}: ')))
      
    if contador == 0:
        maior = valores[contador]
        menor = valores[contador]
        
    else:
        if valores[contador] > maior:
            maior = valores[contador]
            
        if valores[contador] < menor:
            menor = valores[contador]
   
print('-='*30)
print(f'Voce digitou os valores {valores}')
print(f'O maior valor é {maior} nas posicoes ',end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor é {menor} na posicao ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
