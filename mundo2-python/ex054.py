from datetime import date
maior = 0
menor = 0

for pessoa in range (1, 8):
    datanascimento = int(input('Em que ano a {} pessoa nasceu? ' .format(pessoa)))
    idade = date.today().year - datanascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade' .format(maior))
print('E tambem tivemos {} pessoas menores de idade' .format(menor))

    