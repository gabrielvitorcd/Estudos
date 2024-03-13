def fatorial(num = 1, show = False):          #Fatorial de 5:      5 * 4 * 3 * 2 * 1 = 120
    f = 1           #Valor Inicial
    for c in range(num, 0 , -1): #Laco que comeca em num e depois vai lendo de tras para frente
        f *= c              #Opera dentro do laco multiplicando o valor 1 inicial por cada numero do laco 
    return f            #retorna o valor fatorial do numero desejado