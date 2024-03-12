def area(largura,comprimento):
    a = largura * comprimento
    print(f'A area do terreno é : {a:.2f} metros quadrados')


l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))

area(l,c)