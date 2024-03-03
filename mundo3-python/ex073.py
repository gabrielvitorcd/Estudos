times = (
    "Flamengo", "Santos", "Palmeiras", "Grêmio", "Athletico-PR",
    "São Paulo", "Internacional", "Corinthians", "Fortaleza", "Goiás",
    "Bahia", "Vasco", "Atlético-MG", "Fluminense", "Botafogo", "Ceará",
    "Cruzeiro", "CSA", "Chapecoense", "Avaí"
)

listaclassifica = sorted(times)

print(f'Apenas os 5 primeiros colocados {times[0:5]}')
print(f'Os ultimos 4 colocados da tabela {times[-4:]}')
print(f'Uma lista com os times em ordem alfabetica {listaclassifica}')
print(f'Em que posicao está o time da chapecoense {times.index("Chapecoense")}') # O Index so procura com aspas dupla

      