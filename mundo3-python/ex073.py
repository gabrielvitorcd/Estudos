times = (
    "Flamengo", "Santos", "Palmeiras", "Grêmio", "Athletico-PR",
    "São Paulo", "Internacional", "Corinthians", "Fortaleza", "Goiás",
    "Bahia", "Vasco", "Atlético-MG", "Fluminense", "Botafogo", "Ceará",
    "Cruzeiro", "CSA", "Chapecoense", "Avaí"
)

print('-='*30)
print(f'A classificao final de 2019: {times}')
print('-='*30)
print(f'Apenas os 5 primeiros colocados {times[0:5]}')
print('-='*30)
print(f'Os ultimos 4 colocados da tabela {times[-4:]}')
print('-='*30)
print(f'Uma lista com os times em ordem alfabetica {sorted(times)}')
print('-='*30)
print(f'O chapecoense está na {times.index("Chapecoense")+1} posicao') # O Index so procura com aspas dupla

     