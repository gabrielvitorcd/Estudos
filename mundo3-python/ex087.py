todosnum = [[],[],[]]
somapar = 0

for c in range(0,3):
    num = int(input(f'Digite um valor para [0, {c}]: '))
    todosnum[0].append(num)
for c in range(0,3):
    num = int(input(f'Digite um valor para [1, {c}]: '))
    todosnum[1].append(num)
for c in range(0,3):
    num = int(input(f'Digite um valor para [2, {c}]: '))
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

for n in todosnum:
    if n % 2 == 0:
        somapar += n
print(f'a soma dos todos os numeros pares é {somapar}')