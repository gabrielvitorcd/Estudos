nome = str(input('Digite seu nome completo: '))

print('Seu nome em letras maiusculas: {}' .format(nome.upper()))
print('Seu nome em letras minusculas: {}' .format(nome.lower()))

remocao = ''.join(nome.split())
print('Quantidade de letras ao total: {}' .format(len(remocao)))

qtletras = nome.split()
print('Quantidade de letras no primeiro: {}' .format(len(qtletras[0])))