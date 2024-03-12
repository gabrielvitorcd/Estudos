def titulo(txt):
    print('-'*len(txt))
    print(f'{txt}')
    print('-'*len(txt))

def area(largura,comprimento):
    a = largura * comprimento
    print(f'A area do terreno {largura}x{comprimento} é  de {a:.2f} m2')

titulo('   Controle de Terrenos   ')

l = float(input('Digite a largura (m): '))
c = float(input('Digite o comprimento (m): '))

area(l,c)