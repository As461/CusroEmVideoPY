'''
Utilização de metodos modulo Math

radians
sin >> seno
cos >> cosseno
tans >> tangente
'''

##----------------------------------------------------------------##

import math
angulo = float(input('Digite o angulo:'))
seno = math.sin(math.radians(angulo))
print('O ângulo {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo da {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
