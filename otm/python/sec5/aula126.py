class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

dados = {'nome':'GabrielV.','idade': 26}
p1 = Pessoa(**dados)
# p1.nome = 'EITA'
# del p1.nome
# p1.__dict__['outra'] = 'coisa'
# print(p1.__dict__)  #mostra os atributos da classe salvo
# print(p1.outra)
print(vars(p1))