numero_usuario = input('Digite um numero: ')

try:
    numero_usuario = float(numero_usuario)
    if numero_usuario % 2 == 0:
        print('Numero é par')
    else:
        print('Numero é impar')
except:
    print('Erro! Voce nao digitou um numero')