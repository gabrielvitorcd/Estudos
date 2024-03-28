def calculo(numero):
    def calcular(vezes):
        return numero * vezes
    return calcular

num_calculado = int(input('Qual numero deseja calcular:'))
operacao = calculo(num_calculado)
quantidade = int(input('Quantidade de vezes que deseja calcular: '))

print(operacao(quantidade))