# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json



class Pessoa:
    def __init__(self, nome, idade, pais):
        self.nome = nome
        self.idade = idade
        self.pais = pais
    
dados = {'nome':'Gabriel','idade': 25,'pais':'Brasil'}

p1 = Pessoa(**dados)

print(dados)

print(p1.nome)
print(p1.idade)
print(p1.pais)

with open('aula127a.json', 'w',encoding='utf8') as arquivo:
    json.dump(
        dados,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )