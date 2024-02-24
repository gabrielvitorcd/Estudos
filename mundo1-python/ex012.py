preco = float(input('Valor original: R$ '))
liq = preco - (preco * 5/100)

print('Valor real do produto {}' .format(preco))
print('Valor do produto na liquidacao {:.2f}' .format(liq))