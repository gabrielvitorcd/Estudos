expre = str(input('Digite uma expressao matematica: ')) #O PROGRAMA VAI LER UMA EXPRESSAO
pilha = []                       #LISTA QUE VAMOS ADICIONAR CASO TENHA PARENTESES NA LISTA

for simb in expre:                          #FOR VAI VARRER A STRING PODENDO LER CADA ELEMENTO EM LISTA
    if simb == '(':                         #SE O ELEMENTO DA LISTA É IGUAL '(', ELE ADICIONA NA LISTA PILHA 
        pilha.append('(')
    elif simb == ')':                       #SE O ELEMENTO DA LISTA É IGUAL ')' ELE VAI LER SE JA TEM ALGUMN ELEMENTO DENTRO DELA
        if len(pilha) > 0:                  #SE A LISTA TIVER ALGUM ELEMENTO DENTRO QUE SO PODE SER '('
            pilha.pop()                     #ELE VAI REMOVER O ELEMENTO QUE JA TEM NELA
        else:
            pilha.append(')')
            break                           # SE A LISTA ESTIVER VAZIA ELE VAI ADICIONAR UM ELEMENTO NELA


print(pilha)


if len(pilha) == 0:                                 #SE A QUANTIDADE DE ELEMENTO DENTRO DA PILHA É IGUAL A 0
    print('A expressao está correta')
else:                                               #SE NAO ESTIVER VAZIO(CONTEM ALGUM ELEMENTO DENTRO DA LISTA)
    print('A expressao está incorreta')