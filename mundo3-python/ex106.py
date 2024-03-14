c = (
'\033[m', #0 - sem cor
'\033[0;30;41m', #1 - vermelho
'\033[0;30;42m', #2 - verde
'\033[0;30;43m', #3 - amarelo
'\033[0;30;44m', #4 - azul
'\033[0;30;45m', #5 - roxo
'\033[7;30m', #6 - branco
)

def comando(com):
    titulo(f'Acessando o manual do comando \'com\'')
    help(com)
   


def titulo(msg,cor =0):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)
  
    

while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    chamada= str(input("Funcao ou Bibliteca? ")).lower().strip()
    comando(chamada)
    
    if chamada in 'fim':
        break
    else:
        comando(chamada)
titulo('ATÉ LOGO', 1)