"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
#cpf_semponto = cpf.split('.')
#cpf_semtraco = cpf_semponto[2].split('-')
#cpf_limp1 = ''.join(cpf_semponto[:2])
#cpf_limp2 = ''.join(cpf_semtraco)
#cpf_limpo = cpf_limp1 + cpf_limp2
#
#print(cpf_semponto)
#print(cpf_semtraco)
#print(cpf_limpo)
import random
cpf_validados = []
for c in range(1,10001):
    print('-'*30)
    print(f'CPF {c}')
    cpf_sonumeros = ''
    for generator_cpf in range(0,11):
        cpf_sonumeros += str(random.randint(0,9))
    

    print(cpf_sonumeros)

    contador = 10
    soma_todos_num = 0
    for numeros in cpf_sonumeros[:9]:
        numeros_int = int(numeros)
        soma_todos_num += (numeros_int * contador)
        contador -= 1
        
    mult_10 = soma_todos_num * 10
    resto_por_11 = mult_10 % 11

    num_final01 = 0 if resto_por_11 > 9 else resto_por_11
    penultimo_cpf = int(cpf_sonumeros[-2])

    if num_final01 == penultimo_cpf:
        contador = 11
        soma_num2 = 0
        for numeros in cpf_sonumeros[:10]:
            soma_num2 += int(numeros) * contador
            contador -= 1
        soma_num2 *= 10
        resto_somanum2 = soma_num2 % 11
        num_final02 = 0 if resto_somanum2 > 9 else resto_somanum2
        if num_final02 == int(cpf_sonumeros[-1]):
            cpf_validados.append(cpf_sonumeros)
            print('CPF VALIDADO COM SUCECSSO')
        else:
            print('ERRO! SEGUNDO DIGITO NÃO É VALIDO')
    else:
        print('ERRO AO VALIDAR CPF')

print(f'Total de cpf validados: {len(cpf_validados)}')