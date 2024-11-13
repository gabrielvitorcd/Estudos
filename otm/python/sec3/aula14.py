a = 'AAAA'
b = 'BBBBB'
c = 1.141

string = 'a={1},b={0},c={nome3:.2f}'        #posso indicar os indices dessa forma, para chamar a variavel
formato = string.format(a,b,nome3=c)

print(formato)