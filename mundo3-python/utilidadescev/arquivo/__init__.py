def titulo(msg):
    print('-'*30)
    print(f'{msg}'.center(30))
    print('-'*30)

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #abre o arquivo para leitura
        a.close()   #fecha o arquivo
    except FileNotFoundError:       #erro de arquivo nao encontrado
        print('Arquivo nao encontrado: return False')
        return False
    else:
        print('Arquivo encontrado com sucesso: return True')
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #WT+ parametro que cria um arquivo caso nao exister.
        a.close()
    except:
        print('Houve um erro na criacao do arquivo!')
    else:
        print(f'O arquivo {nome} foi criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Nao consegui ler o arquivo')
    else:
        titulo('PESSOAS CADASTRADAS')
        print(a.read())
        

