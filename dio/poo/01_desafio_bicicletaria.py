class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    def buzinar(self):
        print('Buzinei')
    
    def parar(self):
        print('Parei')

    def correr(self):
        print('Correr')

    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"

bicicleta_1 = Bicicleta('Vermelho', 'Caloi 10', 2020, 3000)


print(bicicleta_1)

