nome = str(input('Digite seu nome completo: ')).strip().split()

print('Prazer em te conhecer. ')

print('Seu primeiro nome é {}' .format(nome[0]))

print('Seu ultimo nome é: {}'.format(nome[-1]))


'''
    RESOLUCAO GUANABARA
    FORMATO ANTIGO
    
    
    print('Seu ultimo nome é: {}'.format(nome[len(nome) - 1]) )
    
    Se temos, por exemplo, o nome "MARIA DA SILVA" e a gente usa o SPLIT, o LEN conta a quantidade de palavras começando, obviamente, no "1":
    MARIA = 1
    DA = 2
    SILVA = 3
    Ou seja, o LEN mostra pra gente que existem 3 palavras. 
    MAS na função LISTA, a contagem se inicia no "0". A gente usa a LISTA numa variável que já está SPLITADO (nome) como na linha do Gustavo a seguir:
    print('Seu último nome é {}'.format(nome[ len(nome)-1] )) 
    print('Seu último nome é {}'.format(nome[ 3 - 1 ])) 
    Lembrem-se que a ordem na LISTA da variável (nome) é:
    MARIA = posição 0
    DA = posição 1
    SILVA = posição 2
    Então fazendo o (3 - 1) dentro do parêntesis ficaria:
    print('Seu último nome é {}'.format(nome[2])) que é justamente sempre o último sobrenome nesse exercício.
'''