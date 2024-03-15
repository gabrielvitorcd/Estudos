from utilidadescev import cores

def leiaInt():
  global int
  while True:
    try:
        int = int(input('Digite um Inteiro: '))
        return int          #return cria um break no laco
    except(ValueError,TypeError):
        print(f'{cores.selecionarcor()[1]}ERRO!{cores.selecionarcor()[0]} Digite um número inteiro válido.')
        continue
    except KeyboardInterrupt:
       print(f'\n{cores.selecionarcor()[1]} O usuario preferiu terminar o programa {cores.selecionarcor()[0]}')
       int = 0
       return int
       
   

def leiaFloat():
   global flot
   while True:
    try:        
        flot = float(input('Digite um Real: '))
        return flot
    except KeyboardInterrupt:
        flot = 0
        return flot
    except:      
        print(f'{cores.selecionarcor()[1]}ERRO! Digite um numero real valido {cores.selecionarcor()[0]}')
        continue
        
try:
    divisao = leiaInt() / leiaFloat() 
    print(f'O resultado foi {divisao}')
except ZeroDivisionError:
   print(f'\nA divisao entre {int} e {flot} Nao existe')