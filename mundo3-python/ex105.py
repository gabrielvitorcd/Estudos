def notas(*num):
    resumo = {}
    maior = menor = 0
    for c in num:
        if c > maior:
            maior = c
            menor = c
        if c < menor:
            menor = c

    resumo['total'] = len(num)
    resumo['maior'] = maior
    resumo['menor'] = menor
    resumo['media'] = sum(num)/len(num)
 
    return resumo

resp = notas(5.5,2.5,10,6.5)
print(resp)