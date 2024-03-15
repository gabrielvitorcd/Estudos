
def leiaDinheiro(msg):
    n = str(input(msg)).strip()
    while not n.isnumeric():
        print(f'ERRO: "{n}" é um preco invalido')
        n = str(input(msg)).strip()
    return int(n)
    
