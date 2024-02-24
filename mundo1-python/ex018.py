import math
ang = float(input('Digite o angulo que voce deseja:'))
rad = math.radians(ang)

se = math.sin(rad)
co = math.cos(rad)
ta = math.tan(rad)



print('O angulo de {} tem o SENO de {:.2f}' .format(ang,se))
print('O angulo de {} tem o COSSENO de {:.2f}' .format(ang, co))
print('O angulo de {} tem a tangente de {:.2f}' .format(ang, ta))