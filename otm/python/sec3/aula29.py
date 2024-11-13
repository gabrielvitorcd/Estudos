condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Condicao True')
else:
    print('Condicao False')

if passou_no_if is None:
    print(passou_no_if)
if passou_no_if is not None:
    print(passou_no_if)

print(id(condicao))     #numeracao do espaco guardado na memoria
print(id(passou_no_if))