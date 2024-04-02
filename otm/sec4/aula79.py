# Exemplo de uso dos sets 

letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if letra == 'l':
        print('Final')
        break

    print(letras)