nome = str(input('Insira nome da sua cidade: ')).lower().split()
temsanto = nome[0].find('santo')

if temsanto == 0:
    print('Tem santo no nome')

else:
    print('Nao tem santo no nome')