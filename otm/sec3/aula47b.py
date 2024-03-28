palavra_maquina = 'amor'
acertos = ''    #salva os acertos
while True:
    usuario = input('Digite uma letra:')
    if len(usuario) > 1:
        print('Digite apenas um numeros')
        continue    
    if usuario in palavra_maquina:
        acertos += usuario

    for letra in palavra_maquina:
        if letra in acertos:    #se a letra da palavra bater com os acertos, output: letra 
            print(letra)
        else:
            print('*')                                                      #output: *
        
      

        