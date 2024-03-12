import time

def linha():
    print('-='*30)

def contador(i, f, p):
    linha()
    if p < 0:
        p *= -1         #CONVERTE O PASSO PARA POSITIVO, SE NAO O PROGRAMA RODA ETERNAMENTE QUANDO O PASSO É NEGATIVO
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    cont = i

    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            time.sleep(0.5)
            cont += p
        print(' FIM!')
    else:
        while cont >= f:
            print(f'{cont}' , end=' ', flush=True)
            time.sleep(0.5)
            cont = cont - p
        print(' FIM!')
    linha()

contador(1, 10, 1)
contador(10, 0 ,2)
linha()
print('AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i,f,p)