
def leiaDinheiro(msg):
    n = str(input(msg)).strip().replace(',','.')
    while not n.isnumeric():
        print(f'ERRO: "{n}" é um preco invalido')
        n = str(input(msg)).strip()
    return float(n)
    
