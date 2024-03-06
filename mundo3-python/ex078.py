valores = []
for leitura in range (1,6):
    valores.append(int(input('Digite um numero: ')))

print(f'Os valores sao: {valores}')


for c, v in enumerate(valores):
    valores.sort(reverse=True)
    print(f'O maior valor é {v} na posicao {c}')
    print(f'O menor valor é {valores[-1]}')

print(f'{valores}')
    