from datetime import date

pessoa = {}

pessoa['nome: '] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - ano




print(pessoa)