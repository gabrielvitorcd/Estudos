def linha():
    print('-='*30)

def analise(*val):
    linha()
    print('Analisando os valores passados...')
 
    for c in val:
        print(f'{c}',end=' ')               
    if val[0] == 0:
          print(f' Foram informados {len(val)-1} valores ao todo.') 
    else:
        print(f' Foram informados {len(val)} valores ao todo.')
    print(f'O maior valor informado foi: {sorted(val)[-1]}')
    linha()

analise(2,9,4,5,7,1)
analise(4,7,0)
analise(1,2)
analise(6)
analise(0)