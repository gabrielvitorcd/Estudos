print(True and True and True)

# Avaliacao de curto circuito
print(True and False and True)  #Para no valor False, e retorna ele na expressa. nao lendo o ultimo valor
print(bool(0))  #0 / 0.0 retorna False
print(True and 0 and True)