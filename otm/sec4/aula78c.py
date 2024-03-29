# metodos do set

s1 = set()
s1.add(1)   # .add  -> so adiciona um valor por vez
s1.add(1.5)
s1.add('ABC')
print(s1)   #set nao garante a ordem

s1.update(('Gabriel',15,35))    #adiciona mais valores de uma vez
print(s1)

s1.discard(35)  #descarta um valor do set
s1.discard('Gabriel')
print(s1)
