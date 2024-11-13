# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar'


lista_completa = []
lista_edicao = []


while True:
    print('Comandos: listar, desfazer, refazer')
    resp_usuario = input('Digite uma tarefa ou comando: ')
    
    if resp_usuario == 'listar':
        print('TAREFAS:\n')
        for tarefa in lista_completa:
            print(tarefa)
        continue
    elif resp_usuario == 'desfazer':
        lista_edicao.append(lista_completa[-1])
        lista_completa.pop()
        continue

    elif resp_usuario == 'refazer':
        if len(lista_edicao) == 0:
            print('NADA PRA REFAZER MANO')
        lista_completa.append(lista_edicao[-1])
        lista_edicao.pop()
        continue
    
    elif resp_usuario	== 'sair':
        break
    
    else:           
        try:
            lista_completa.append(resp_usuario)
        except:
            print('deu ruim mano')
        
        
    