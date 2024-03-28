import os

while True:
    lista_de_compras = []
    print('Selecione uma opção')
    menu_lista = input('[i]nserir [a]pagar [l]istar: ').lower().strip()

    if len(menu_lista) > 1:
        continue

    if menu_lista == 'i':
        os.system('clear')
        lista_de_compras.append(input('Valor: '))
        continue
    elif menu_lista == 'a':
        os.system('clear')
        item_apagar = input('Escolha o índice para apagar: ')
        try:
            item_apagar = int(item_apagar)
            lista_de_compras.pop(item_apagar)
            print('Item removido com sucesso')
        except:
            print('Não foi possível apagar este índice')
    elif menu_lista == 'l':
        if len(lista_de_compras) == 0:
            os.system('clear')
            print('Nada para lista')
            continue
        else:
            os.system('clear')
            for indice, valor in enumerate(lista_de_compras):
                print(indice,'->',valor)
            continue
    else:
        os.system('clear')
        print('Insira uma opção valida')
        continue
    
    
    
