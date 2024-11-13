class Pessoa:
    ano = 2024  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod    #decorator que serve pra chamar a funcao sem dar o parametro
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod    #cria uma nova instancia da classe com mais de 50 anos
    def criar_pessoa_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod    
    def criar_sem_nome(cls, idade):
        return cls('Anonima', idade)


p1 = Pessoa('Vitor', 26)
print(p1.nome, p1.idade)

p2 = Pessoa.criar_pessoa_50_anos('Helena')
print(p2.nome, p2.idade)

p3 = Pessoa('Anonima', 23)
print(p3.nome, p3.idade)

p4 = Pessoa.criar_sem_nome(30)
print(p4.nome, p4.idade)



# print(Pessoa.ano)
# Pessoa.metodo_de_classe()

     