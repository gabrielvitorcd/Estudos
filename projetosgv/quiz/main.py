#BUZZFEED QUE JOGADOR VOCE É
from material import *

rp = []

def resposta(msg):
    while True:
        try:
            n = int(input(msg))
            if n>2 or n < 1:
                print('SOMENTE NUMERO 1 ou 2')
                continue
        except:
            print('ERRO! DIGITE UM NUMERO VALIDO')
        else:
            rp.append(n)
            return rp


titulo('BUZZFEED')
for c in range(0,4):
    titulo(pergunta()[c])
    print('''
[1] - SIM 
[2] - NAO''') 
    resp = resposta('DIGITE SUA RESPOSTA: ')

if resp == [1, 1, 1, 1]:
    titulo('Você é como o "Lionel Messi", conhecido por sua extrema habilidade, liderança dentro e fora do campo, espírito de equipe e competitividade inigualável.')
elif resp == [1, 1, 1, 2]:
    titulo('Você é como o "Cristiano Ronaldo", com um estilo de vida extravagante, liderança em campo, mas menos focado no trabalho em equipe.')
elif resp == [1, 1, 2, 1]:
    titulo('Você é como o "Neymar", talentoso, líder quando necessário, mas às vezes se envolve em polêmicas e tem um lado mais individualista.')
elif resp == [1, 1, 2, 2]:
    titulo('Você é como o "Zlatan Ibrahimović", um líder forte e competitivo, mas nem sempre focado no bem-estar dos outros.')
elif resp == [1, 2, 1, 1]:
    titulo('Você é como o "Andrés Iniesta", discreto, mas extremamente talentoso, e sempre disposto a ajudar os companheiros de equipe.')
elif resp == [1, 2, 1, 2]:
    titulo('Você é como o "Xavi Hernández", focado no jogo em equipe e ajudando os outros, mas menos extrovertido.')
elif resp == [1, 2, 2, 1]:
    titulo('Você é como o "Sergio Ramos", competitivo e disposto a liderar, mas nem sempre preocupado com o bem-estar dos outros.')
elif resp == [1, 2, 2, 2]:
    titulo('Você é como o "Gianluigi Buffon", um líder tranquilo e focado em seu desempenho, mas menos extrovertido.')
elif resp == [2, 1, 1, 1]:
    titulo('Você é como o "Manuel Neuer", um líder dentro e fora de campo, sempre focado no bem-estar do time e extremamente competitivo.')
elif resp == [2, 1, 1, 2]:
    titulo('Você é como o "Virgil van Dijk", um líder forte e focado, mas menos interessado em ajudar os outros fora do campo.')
elif resp == [2, 1, 2, 1]:
    titulo('Você é como o "Luis Suárez", competitivo e talentoso, mas às vezes envolvido em polêmicas e menos preocupado com o bem-estar dos outros.')
elif resp == [2, 1, 2, 2]:
    titulo('Você é como o "Diego Costa", competitivo e agressivo, com menos preocupação com o bem-estar dos outros.')
elif resp == [2, 2, 1, 1]:
    titulo('Você é como o "David Silva", talentoso e focado no jogo em equipe, mas menos extrovertido e competitivo.')
elif resp == [2, 2, 1, 2]:
    titulo('Você é como o "Andrea Pirlo", discreto e talentoso, com uma abordagem tranquila e focada no jogo em equipe.')
elif resp == [2, 2, 2, 1]:
    titulo('Você é como o "Gianluigi Donnarumma", discreto e talentoso, focado em seu desempenho individual, mas menos extrovertido.')
elif resp == [2, 2, 2, 2]:
    titulo('Você é como o "Cesc Fàbregas", discreto e talentoso, com uma abordagem tranquila e menos competitiva.')
