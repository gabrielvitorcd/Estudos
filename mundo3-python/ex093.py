jogador = dict()
soma = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas zico jogou? '))

for c in range(0,partidas):
    jogador['gols'] = int(input(f'Quantos gols na partida {c}? '))
    soma += jogador['gols']
    jogador['total'] = soma
print(soma)
print(jogador)