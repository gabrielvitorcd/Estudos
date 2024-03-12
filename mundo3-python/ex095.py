jogador = dict()
partida = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(0,tot):
        partida.append( int(input(f'Quantos gols na partida {c+1}? ')))
        
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    
    time.append(jogador.copy())

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

for i, v in enumerate(time):
    print(f'{i}' , end='')
    for v in v.values():
        print(f'   {v}' , end='  ')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols ')