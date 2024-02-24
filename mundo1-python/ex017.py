import math

co = float(input('Insira o cateto oposto: '))
ca = float(input('Insira o cateto adjacente: '))

hi = math.hypot(co, ca)
''' hi = (co **2 + ca **2) ** (1/2)'''
print('A hipotenusa vai medir: {:.2f}' .format(hi))

