import moeda

p = float(input('Digite o preco: R$ '))
print(f'A metade {p} é {moeda.formatacao(moeda.metade(p))}')
print(f'O dobro de {p} é {moeda.formatacao(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.formatacao(moeda.aumentar(p,10))}')
print(f'Reduzindo 13%, temos {moeda.formatacao(moeda.diminuir(p,13))}')