#como 'for...' funciona dentro do pc
"""
Iterável -> str, range, lista, tupla, dicionarios e etc. (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entre seu iterador
"""

#for letra in texto
texto = 'Luiz'  #iterável
iteratador = iter(texto)    #iterator

while True:
    try:
        print(next(iteratador))
    except StopIteration:
        break