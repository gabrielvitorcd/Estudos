import json



class Pessoa:
    def __init__(self, nome, idade, pais):
        self.nome = nome
        self.idade = idade
        self.pais = pais


with open('aula127a.json', 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)

p2 = Pessoa(**dados)

print(p2.nome)
print(p2.idade)
print(p2.pais)