from utilidadesex107 import moeda

p = float(input('Digite o preco: R$ '))
print(f'A metade {p} é {moeda.metade(p,False)}')
print(f'O dobro de {p} é {moeda.dobro(p,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10,True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13,True)}')