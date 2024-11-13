def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar       #Os parametros das funcao eu insiro abaixo

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Bom noite')


print(falar_bom_dia('Luiz'))
print(falar_boa_noite('Maria'))

# Codigo que cria funcao dentro de outra funcao