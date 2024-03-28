# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Gabriel Vitor'
pessoa['sobrenome'] = 'Oliveira'

lista = []


del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:     #.get retorna se valor é None(Nao existe)
                                        # se existir o valor é not None(existe/foi encontrado algum valor)
    print('Nao existe')
else:
    print('Existe')
print(pessoa[chave])

var = pessoa.get('nome')

print(var)