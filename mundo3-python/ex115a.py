def selecionarcor():
    c = [
    '\033[m',          # 0 - sem cor (fundo normal, letras normais)
    '\033[0;31m',      # 1 - vermelho
    '\033[0;32m',      # 2 - verde
    '\033[0;33m',      # 3 - amarelo
    '\033[0;34m',      # 4 - azul
    '\033[0;35m',      # 5 - roxo
    '\033[0;37m',      # 6 - branco
    ]
    return c

def linha():
    print('-'*30)

def titulo(msg):
    linha()
    print(f'{msg}'.center(30))
    linha()

def menu():
    titulo('MENU PRINCIPAL')
    print(f'''
{selecionarcor()[3]} 1 {selecionarcor()[0]}{selecionarcor()[4]}- Ver pessoas cadastradas
{selecionarcor()[3]} 2 {selecionarcor()[0]}{selecionarcor()[4]}- Cadastrar nova Pessoa
{selecionarcor()[3]} 3 {selecionarcor()[0]}{selecionarcor()[4]}- Sair do Sistema''')
    linha()
    


menu()
while True:
    try:
        resp = int(input(f'{selecionarcor()[2]} Sua Opcao: {selecionarcor()[0]}'))
        if resp > 3 or resp < 1:
            print('Digite um numero valido')
    except:
        print(f'{selecionarcor()[1]}ERRO! por favor, digite um numero valido(1 a 3){selecionarcor()[0]}')
        continue
    else:
        if resp == 1:
            titulo('OPCAO 1')
            break
        if resp == 2:
            titulo('OPCAO 2')
            break
        if resp == 3:
            print('Voce saiu do programa com sucesso')
            break
