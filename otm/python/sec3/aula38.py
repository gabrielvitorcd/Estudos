qtd_linhas = 5
qtd_coluna = 5

linha = 1


while linha <= qtd_linhas:
    
    coluna = 1 
    while coluna <= qtd_coluna:
        print(f'{coluna=}{linha=}')
        coluna += 1
    linha += 1
    
    
print('Acabou o laço')