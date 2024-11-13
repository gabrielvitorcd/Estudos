numero_1 = input('Digite o numero 1: ')   
numero_2 = input('Digite o numero 2: ')

if numero_1.isnumeric() and numero_2.isnumeric():
    print('Numero digitado com sucesso')
    numero_1 = int(numero_1)
    numero_2 = int(numero_2)
else:
    print('Digite um numero valido, para que nao acontecao a concatenacao')
print(f'A soma é {numero_1 + numero_2}')