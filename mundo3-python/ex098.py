import time

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for c in range(i, f+1, p):
        print(f' {c}', end='->')
        time.sleep(1)
    print(' FIM!')
        

contador(1, 10, 1)

