def multiplicacao(*args):
    total = 1
    for num in args:
        total *= num
    return total

resultado = multiplicacao(1,2,3,4,5,6,7,8)

def parouImpar(x):
    if x % 2 == 0:
        print('PAR')
    else:
        print('IMPAR')

print(resultado)
parouImpar(resultado)
