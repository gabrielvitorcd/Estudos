def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao,*texto):
    return funcao(*texto)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao,'Boa noite','Maria')
)