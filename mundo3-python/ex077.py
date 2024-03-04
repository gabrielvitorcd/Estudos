palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')

print(palavras)

for pos in palavras:
    print(f'\nNa palavra {pos} temos ', end='')
    for letra in pos:
        if letra.upper() in 'AEIOU':
            print(f' {letra} ', end='')