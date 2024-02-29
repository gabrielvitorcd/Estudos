primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimotermo = primeirotermo + (10 - 1) * razao #FORMULA PRA CALCULAR OS 10 TERMOS 

for c in range (primeirotermo, decimotermo + razao, razao):
    print('{}' .format(c), end= ' > ')
print('ACABOU')