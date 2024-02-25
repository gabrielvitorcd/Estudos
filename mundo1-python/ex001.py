import time
print('='*20,'Desafio 01','='*20)

nome = input('Qual seu nome? ')

print('Processando...')
time.sleep(1)

print('É um prazer te conhecer, \033[32m{}\033[m !' .format(nome))