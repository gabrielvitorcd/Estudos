maior = 0
menor = 0
lista = []

for c in range(0,5):
    n = int(input(f'Valor {c}: '))

    if c == 0 or n > lista [-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        
        pos = 0
        while pos < len(lista):

            if n <= lista[pos]:
            
                lista.insert(pos, n)
                print(f'Adicionado na posicao {pos} da lista')
                break
            pos += 1

print(f'Lista Completa: {lista}')