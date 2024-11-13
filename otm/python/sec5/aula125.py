class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(f'{self.nome} Nasceu em:', end=' ')
        return Pessoa.ano_atual - self.idade
    


p1 = Pessoa('Gabriel',26)
p2 = Pessoa('Gaby', 25)

print('Ano Atual: ',Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())