'''
Utilização do metodo
Shuffle na biblioteca random
'''

import random
aluno1 = input('Digite o nome do 1º aluno: ')
aluno2 = input('Digite o nome do 2º aluno: ')
aluno3 = input('Digite o nome do 3º aluno: ')
aluno4 = input('Digite o nome do 4º aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print('Ordem sorteada de apresentação:')
print(f'1º: {alunos[0]}')
print(f'2º: {alunos[1]}')
print(f'3º: {alunos[2]}')
print(f'4º: {alunos[3]}')

