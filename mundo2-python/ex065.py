soma = 0
totallacos = 0
resposta = 's'



while resposta in 'Ss' :
    numero = int(input('Digite um numero: '))
    resposta = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    totallacos += 1
    soma += numero

    if totallacos == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        

media = soma / totallacos    
print(f'Voce digitou {totallacos} numeros e a media foi {media}' )
print('O maior valor digitado foi {} e o menor foi {}' .format(maior, menor))