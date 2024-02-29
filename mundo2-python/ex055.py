lista = []

for pessoa in range(1, 6):
    peso = float(input('Peso da {} pessoa: ' .format(pessoa)))
    lista = lista + [peso] #ADICIONA PESO DENTRO DA LISTA

lista.sort() #COLOCA A LISTA EM ORDEM CRESCENTE

print('O maior peso lido foi de {}Kg' .format(lista[-1])) #MOSTRA O ULTIMO ITEM DA LISTA CRESCENTE(MAIOR ITEM)
print('O menor peso lido foi de {}Kg' .format(lista[0])) #MOSTRA O PRIMEIRO ITEM DA LISTA CRESCENTE(MENOR ITEM)

