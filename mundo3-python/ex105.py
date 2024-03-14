def notas(*num,sit = False):
    """
    notas(*n , sit=False)
        ->Funcao para analisar notas e situacoes de varios alunos.
        :parametro n: uma ou mais notas dos alunos (aceita varias)
        :parametro sit: Valor opcional,indicando se deve ou nao adicionar a situacao
        :return: dicionario com varias informacoes sobre a situacao da turma.    
     """
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
    if sit == True:
        if resumo['media'] >= 7:
            resumo['situacao'] = 'Aprovado'
        else:
            resumo['situacao'] = 'Reprovado'
    return resumo

resp = notas(5.5,2.5,10,6.5,)
print(resp)
