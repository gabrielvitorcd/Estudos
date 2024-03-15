def metade(n,format=False):
    met = n /2
    if format == False:
        return met
    if format == True:
        return f'R${met:.2f}'

def dobro(n,format=False):
    dob = n * 2 
    if format == False:
        return dob
    if format == True:
        return f'R${dob:.2f}'

def aumentar(n,adi,format=False):
    adi /= 100
    aumento = n + (n * adi)
    if format == False:
        return aumento
    if format == True:
        return f'R${aumento:.2f}'

def diminuir(n, sub,format=False):
    sub /= 100
    dimi = n - (n * sub)
    if format == False:
        return n - (n * sub)
    if format == True:
        return f'R${dimi:.2f}'

def formatacao(ft):
    return f'R${ft:.2f}'
        


def resumo(n,at=1,rd=1):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print('Preco analisado:', f'{formatacao(n):>7}')
    print('Dobro do preco: ', f'{dobro(n,True):>7}')
    print('Metade do preco:', f'{metade(n,True):>7}')
    print('80% de aumento: ', f'{aumentar(n,at,True):>7}')
    print('35% de reducao: ', f'{diminuir(n,rd,True):>7}')
    print('-'*30)

