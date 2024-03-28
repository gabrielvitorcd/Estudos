nomes = ['Maria', 'Helena', 'Luiz']

_,nome1, * _ = nomes  # * cria uma lista com os restos dos valores
# se nao for usar o resto dos valores, por convenção chamamos esse resto não utilizavel de _

print(nomes)
print(nome1)
print(_)

