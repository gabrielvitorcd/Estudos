import time
num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))
opcao = 0

while opcao != 5:

    opcao = int(input('''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
>>>>> Qual é a sua opcao? '''))

    if opcao == 1:
        soma = num1 + num2
        print('SOMAR: {} + {} = {}' .format(num1, num2, soma))
    elif opcao == 2:
        multiplicacao = num1 * num2
        print('MULTIPLICAR: {} x {} = {}' .format(num1, num2, multiplicacao ))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior é {}' .format(num1, num2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opcao Invalidade digite novamente')

    print('=--='*15)
    time.sleep(2)
print('Programa Finalizado, Volte sempre')