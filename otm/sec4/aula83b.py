pessoa = {
    'nome':'Aline',
    'sobrenome':'Souza',
} 

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}   #desempacotamento de dicionario

# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments(argumentos nomeados)

def mostro_argumentos_nomeados(*args,**kwargs):
    print('Nao NOMEADOS:',args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Joana', qlq=123)
print()
mostro_argumentos_nomeados(**pessoas_completa)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)