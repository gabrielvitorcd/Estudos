print('Gerador de PA')
print('-=' *10)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))

pa = primeiro 
c = 1

while c <= 10:
    
    print(' {} ->' .format(pa), end='')
    pa += razao
    c += 1

print(' PAUSA')

