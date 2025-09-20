a = float(input('Qual é a altura da parede? '))
c = float(input('Qual é o comprimento da parede? '))
mq = a * c
s = mq / 2
print('Sua parede tem a dimensão de {} X {}'.format(a, c))
print('Você precisara de {} litros de tinta para pintar a parede'.format(s))