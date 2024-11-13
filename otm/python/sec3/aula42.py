frase  = 'Gabriel Vitor Gomes de Oliveira'.upper()
contagem = ''

i = 0
oque_contar = input('Oque voce quer contar: ').upper()

while i < len(frase):
    letra_atual = frase[i]
    

    if letra_atual == oque_contar:
        contagem += letra_atual

    print(letra_atual)
    i += 1

print(
    'A contagem foi realizado com sucesso\n'
    f'Voce está procurando "{oque_contar}"\n'
    f'Foi encontrado {len(contagem)}x\n'
    f'{contagem=}'
      )