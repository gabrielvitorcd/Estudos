precos = ('Lapis',1.75,
          'Borracha',2.0,
          'Caderno',15.9,
          'Estojo',25,
          'Transferidor',4.2,
          'Compasso',9.99,
          'Mochila',120.32,
          'Canetas',22.30,
          'Livro',34.90 )

print(f'{precos[0]}...............{precos[1]}')
print(f'{precos[2]}...............{precos[3]}')
print(f'{precos[4]}...............{precos[5]}')
print(f'{precos[6]}...............{precos[7]}')
print(f'{precos[8]}...............{precos[9]}')
print(f'{precos[10]}..............{precos[11]}')
print(f'{precos[12]}..............{precos[13]}')
print(f'{precos[14]}..............{precos[15]}')
print(f'{precos[16]}..............{precos[17]}')



for pos in range (0, len(precos)):
    if pos % 2 == 0:
        print(f'{precos[pos]:.<30}',end='')
    else:
        print(f'R${precos[pos]:>7.2f}')