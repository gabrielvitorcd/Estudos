def linha():
    print('-'*40)

pessoa = {
    'nome':'Luiz Otavio',
    'sobrenome':'Miranda',

}
linha()
print(pessoa.__len__())     #faz a mesma coisa
print(len(pessoa))
linha()
#keys
print(pessoa.keys())    #retorna as keys do dict(pessoa)
print(list(pessoa.keys())[0])    #converte em lista o metodo keys
linha()
#values
print(pessoa.values())      #retorna os values do dict(pessoa)
print(list(pessoa.values())[1])
linha()
#items
print(pessoa.items())   #retorna chave e valor
linha()
print('start do for')
for chave in pessoa:
    print(chave)
linha()
#setdefault
pessoa.setdefault('idade', 900.5)   #se nao tiver criado a chave, atribui um valor padrao   
print(type(pessoa['idade']))