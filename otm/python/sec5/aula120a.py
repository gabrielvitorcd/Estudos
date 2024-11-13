#cria a classe pessoa. sempre por convencao primeira letra da de cada palavra é maiuscula 
class Pessoa:
    ...


p1 = Pessoa()   #cria a primeira instancia da classe
p1.nome = 'Gabriel'    #atribui o atributo(caracteristica) [nome]
p1.sobrenome = 'Vitor'    #atribui o atributo(caracteristica) [sobrenome]


p2 = Pessoa()   #cria a segunda instancia da classe
p2.nome = 'Maria'    #atribui o atributo(caracteristica) [nome]
p2.sobrenome = 'Joaquina'    #atribui o atributo(caracteristica) [sobrenome]


print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)