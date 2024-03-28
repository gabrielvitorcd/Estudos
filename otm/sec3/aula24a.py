# Operadores in e not in
# Strings sao iteraveis(voce pode navegar dentro deles)
# 0 1 2 3 4 5   - indices positivos
# O t a v i o
#-6-5-4-3-2-1   -indices negativo da string otavio

nome = 'Otávio'

print(nome[2]) 
print(nome[-4])
print('á' in nome) #-> 'á' está dentro de nome -> retorna True
print('zero' in nome)  #-> nao está dentro de nome -> retorna False
print('vio' not in nome)  #Checa se 'vio' nao está dentro de nome -> retorna false