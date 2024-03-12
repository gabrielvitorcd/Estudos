jogador = dict()
partida = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0,tot):
    partida.append( int(input(f'Quantos gols na partida {c}? ')))
    
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(partida)} partidas.')
for indice, valor in enumerate(partida):
    print(f' » Na partida {indice}, fez {valor} gols')
print(f'Foi um total de {jogador["total"]} gols')