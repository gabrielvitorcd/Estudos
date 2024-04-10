def linha():
    print('-'*40)

a,b = 1,2
a,b = b,a

print(f'A vale [{a}] / B vale [{b}]')

pessoa = {
    'nome':'Aline',
    'sobrenome':'Souza',
}

linha()
a,b = pessoa
print(a)
print(b)
linha()

a,b = pessoa.values()
print(a)
print(b)
linha()

a,b = pessoa.items()
print(a)
print(b)
linha()

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments(argumentos nomeados)