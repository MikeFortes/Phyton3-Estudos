
# ! Desafio 19
# ! Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

import random

a = input(' Digite o nome do primeiro aluno: ')
b = input(' Digite o nome do segundo aluno: ')
c = input(' Digite o nome do terceiro aluno: ')
d = input(' Digite o nome do quarto aluno: ')

esc = random.choice([a, b, c, d])
print('O aluno escolhido foi {}'.format(esc))