nome = input('Digite seu nome completo: ').strip().lower()
idade = input('Digite sua idade: ').strip().lower()

if nome and idade:          #Se o usario nao digitar nada, sera considerado vazio e retorna False, invalidando esse if
    print(f'O seu nome é {nome}')
    print(f'O seu nome é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome tem espaco')
    else:
        print('Seu nome nao tem espaco')
    print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
    print(f'A primeira letra de {nome} é {nome[0]}')
    print(f'A ultima letra de {nome} é {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios')