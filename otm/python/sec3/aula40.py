#Calculadora
while True:
    numero_1 = input('Digite um numero 1: ')
    numero_2 = input('Digite um numero 2: ')
    
    try:
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
    except:
        print('Voce esqueceu de digitar um numero ou não digitou. Tente Novamente')
        continue
    
    operacao = input('Digite o sinal da operação que deseja fazer -> ')

    if operacao == '+':
        print('Voce quer fazer adição')
        break
    elif operacao == '-':
        print('Voce quer fazer subtração')
        break
    elif operacao == '*':
        print('Voce quer fazer multiplicação')
        break
    elif operacao == '/':
        print('Voce quer fazer divisão')
        break
    else:
        print('Só realizo operações com + - * /')
        print('Voce nao digitou uma operacao valida.')