nomecompleto = str(input('Insira seu nome completo: ')).lower()
temsilva = 'silva' in nomecompleto

if temsilva == True:
    print('Parabens, seu nome tem silva')

else:
    print('Infelizmente seu nome nao tem silva')



'''
    RESOLUCAO GUANABARA:
    
    nome = str(input('Qual é seu nome completo')).strip()
    print('Seu nome tem Silva? {}' .format('silva' in nome.lower()))

'''