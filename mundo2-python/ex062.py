print('Gerador de PA v2.0')
print('-=' * 10)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))

pa = primeiro
c = 1
mais = 10
total = 0


while mais != 0:

    total = total + mais
    while c <= total:

        print(' {} ->' .format(pa), end='')
        pa += razao
        c += 1
        
    print(' PAUSA')
    mais = int(input('Quantos termos voce quer a mais? '))


print('Progressao finalizada com {} termos mostrados' .format(total))
