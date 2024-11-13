"""
. <numero de digitos>f
x ou X -Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal + ou -
Ex : 0>-100,.1f
Conversion flags !r/!s !a  
"""
texto = 'Titulo'
print(f'{texto:^20}')   # Centraliza a string em 20 caracteres, 10 espacos para a esquerda e 10 pra direita
print(f'{texto:>20}')   # Comeca 20 caracteres a esquerda
print(f'{texto:<20}')   # Comeca 20 caracteres a direita
print(f'{texto:*>20}')  # Insere 20 * a esquerda
print(f'{texto:@<20}')  # Insere 20 @ a direita