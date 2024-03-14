def partida(nome ,gol):
    if len(nome) == 0:
        nome = '<desconhecido>'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

jogador = str(input('Nome do Jogador: '))
resultado = str(input('Numero de Gols: '))

partida(jogador,resultado )