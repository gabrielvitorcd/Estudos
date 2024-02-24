print('PROGRAMA PARA PINTORES!\nInsire as medidas necessarias para o calculo')


largura = float(input('Digite a largura da area: '))
altura = float(input('Digite a altura da area: '))
area = largura * altura
tinta = area / 2

print('A area do espaco a ser pintado {:.1f} metros quadrados'.format(area) )
print('Serao necessarias {:.1f}l de tinta' .format(tinta))