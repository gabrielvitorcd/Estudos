todosnum = [[], [], []]
somapar = 0
somacoluna = 0
maior = 0

for c in range(0, 3):
    num = int(input(f'Digite um valor para [0, {c}]: '))
    if num % 2 == 0:
        somapar += num
    todosnum[0].append(num)
for c in range(0, 3):
    num = int(input(f'Digite um valor para [1, {c}]: '))
    if num > maior:
        maior = num
    if num % 2 == 0:
        somapar += num
    todosnum[1].append(num)
for c in range(0, 3):
    num = int(input(f'Digite um valor para [2, {c}]: '))
    if num % 2 == 0:
        somapar += num
    todosnum[2].append(num)

print('-='*30)

for n in todosnum[0]:
    print(f'[ {n} ]', end='')
print()

for n in todosnum[1]:
    print(f'[ {n} ]', end='')
print()

for n in todosnum[2]:
    print(f'[ {n} ]', end='')
print()

print(f'a soma dos todos os numeros pares é {somapar}')
for s in todosnum:
    somacoluna += s[2]
print(f'A soma dos valores da terceira coluna é {somacoluna}')
print(f'O maior valor da segunda linha é {maior}')
