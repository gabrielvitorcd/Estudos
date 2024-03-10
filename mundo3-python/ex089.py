dado = []
alunos = []
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Nota 1: ')))
    dado.append(float(input('Nota 2: ')))
    alunos.append(dado[:])
    dado.clear()

    saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if saida == 'N':
        break

print('-='*40)
print('-'*25)
for i, v in enumerate(alunos):
    print(f'{i}   {v[0]}    {(v[1]+v[2])/2}')
print('-'*25)

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if mostrar == 999:
        break

    while mostrar > (len(alunos) - 1):
        mostrar = int(
            input('Esse aluno nao existe, digite novamente. (999 interrompe): '))
        if mostrar == 999:
            break

    print(f'Notas de {alunos[mostrar][0]} sao {alunos[mostrar][1:]}')

    if mostrar == 999:
        break
