'''
--- HYPOT (Hipotenusa)
hypot ( , )
Função do modulo math para calcular a hipotenusa
'''


##------------------------------- Metodo 1 (Sem Modulo) ----------------##
'''
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('{:.2f}'.format(hi))
'''
##------------------------------- Metodo 2 (Modulo) ----------------##
import math
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
hi = math.hypot(co, ca)
print('{:.2f}'.format(hi))
