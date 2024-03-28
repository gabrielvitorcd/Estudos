#range(start,stop,step)
numeros = range(0,11,2)         #step positivo contagem crescente

for numero in numeros:
    print(numero)


print('separacao')
numeros = range(11,0,-1)   #step negativo contagem decrescente, tem que inverter o inicio e fim.

for numero in numeros:
    print(numero)

print('separacao')
numeros = range(0,-11,-2) 

for numero in numeros:
    print(numero)