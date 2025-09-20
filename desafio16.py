##--------------------------Funções---------------------------------##
'''
---- Ceil
A função JavaScript Math.ceil () arredonda um determinado número para o inteiro mais próximo.
Ele sempre arredonda para o infinito positivo, o que significa que aumenta o número para o próximo número inteiro,
se ainda não for um número inteiro. Esta função é útil para arredondar valores em cálculos.

---- Trunc
Para retornar a parte inteira de um valor numérico em JavaScript, você pode usar o método Math.trunc().
Este método foi adicionado ao objeto Math na versão ECMAScript 2015, ou ES6, e é útil para remover a parte fracionária de
um número sem arredondar. O método Math.trunc() é uma maneira simples e direta de obter a parte inteira de um número, ideal para
situações onde você precisa de um valor inteiro sem considerar o valor decimal.
'''

##----------------------------- Metodo 1 ----------------------------##
'''from math import ceil
num = float(input('Digite um numero:'))
print('O numero {} team a parte inteira {} '.format(num, ceil(num)))
'''
##------------------------------ Metodo 2 ---------------------------##
'''import math
num = float(input('Digite um numero:'))
print('O valor {} tem a parte inteira {}'.format(num, math.trunc(num)))
'''
##------------------------------- Metodo 3 --------------------------##
num = float(input('Digite um numero:'))
print('O valor {} tem a parte inteira {}'.format(num, int(num)))
