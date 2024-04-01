# Operadores úteis:
# uniao | uniao (union)- Une
# interseccão & (intersection) - Itens presentes em ambos
# diferenca -  itens presentes apenas no set da esquerda
# dirferenca simetrica - itens que nao estao em ambos


s1 = {1,2,3}
s2 = {2,3,4}

s3 = s1 | s2    #Une todos os elementos
s4 = s1 & s2    #Item em comuns de ambos
s5 = s1 - s2    #Itens diferente apenas do set da esquerad


# s4 = s1.difference(s2)    #itens or
# s4 = s1.symmetric_difference(s2)    #itens que nao estao na lista

print(s3)
print(s4)
print(s5)