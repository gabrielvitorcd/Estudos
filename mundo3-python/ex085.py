todosnum = [[],[]]

for c in range(1,8):
    num = int(input(f'Digite um valor {c}: '))

    if num % 2 == 0:
        todosnum[0].append(num)
    else:
        todosnum[1].append(num)



print(f'Os valores pares digitados foram: {sorted(todosnum[0])}')
print(f'Os valores impares digitados foram: {sorted(todosnum[1])}')
