def linha():
    print('-='*30)

def analise(*val):
    linha()
    print('Analisando os valores passados...')
    maior = 0
    cont = 0
    for c in val:
        print(f'{c}',end=' ')               
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    linha()

analise(2,9,4,5,7,1)
analise(4,7,0)
analise(1,2)
analise(6)
analise()