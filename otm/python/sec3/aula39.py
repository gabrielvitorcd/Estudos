nome = 'Luiz Otavio'

print(f'A string é [{nome}]')

contador = 0
novo_nome = ''

while contador < len(nome):
    letra = f'*{nome[contador]}'
    novo_nome += letra
    contador += 1


print(novo_nome)