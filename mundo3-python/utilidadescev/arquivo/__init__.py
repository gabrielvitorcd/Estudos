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
        for linha in a:         #converte em lista
            dado = linha.split(';') #remove o ; que separa
            dado[1] = dado[1].replace('\n','') #remove \n que foi inserido no write do cadastro 
            print(f'{dado[0]}\t\t\t{dado[1]} anos')
    finally:
        a.close()

def gravarArquivo(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq, 'a')
    except:
        print('ARQUIVO NAO ENCONTRADO')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO! AO ESCREVER ESSE PROGRAMA')
        else:
            print(f'Novo registro de {nome} adicionado')