class Pessoa:
    #a primeira funcao tem que ser __init__ com self
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    


p1 = Pessoa('Gabriel','Vitor')   
   


p2 = Pessoa('Maria','Joaquina')   
   

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)