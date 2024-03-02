sexo = str(input('Informe seu sexo [M/F]: ')).upper()

while sexo not in 'MF':
    sexo = str(input('Codigo Invalido, Digite o sexo [M/F]: ')).upper()
    

print('Sexo digitado Corretamente')
