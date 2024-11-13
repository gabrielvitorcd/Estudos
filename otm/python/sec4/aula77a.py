perguntas = [

    {
        'Pergunta': 'Quanto é 2 + 2 ?',
        'Opcoes': ['1','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5 ?',
        'Opcoes': ['25','55','10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opcoes': ['4','5','2','1'],
        'Resposta': '5',
    },
]
acertos = 0
for contador in range(len(perguntas)):
    pergunta_atual = perguntas[contador]    
    print(pergunta_atual['Pergunta'])
    print()
    for i,v in enumerate(pergunta_atual['Opcoes']):
        print(f'{i}) {v}') 
        
    try:
        resp = input('Escolha uma opcao: ')
        resp = int(resp)
        if pergunta_atual['Opcoes'][resp] == pergunta_atual['Resposta']:
            print('Acertou Mizeravel')
            acertos += 1
        else:
            print('ERRO! Mizeravel')
    except:
        print('ERRO')    
    print()


print(f'Voce acertou {acertos} de {len(perguntas)}')