nome_usuario = input('Digite o nome do usuario: ')

if len(nome_usuario) <= 4:
    print('Seu nome é curto')
elif len(nome_usuario) == 5 or len(nome_usuario)==6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande!')