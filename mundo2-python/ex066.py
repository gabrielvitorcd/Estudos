soma = 0
while True:
    num = int(input('Digite um numero: '))
    soma += num
    if num == 999:
        break

print(f'FIM Total de numero sem o flag: {soma-999}')