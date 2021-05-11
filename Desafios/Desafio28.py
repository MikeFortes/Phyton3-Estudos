
# ! Desafio 28
# ! Crie um programa que faça seu computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador. Informar se o usuario venceu ou perdeu.

import random
x = random.randint(0, 5)
print('-=-' * 20)
num = int(input('Hey você! De 1 a 5, qual numero estou pensando? '))
print('-=-' * 20)
if num == x:
    print('Parabens, você advinhou, eu estava pensando no numero {}'.format(x))
else:
    print('HAHAHA Você perdeu, o numero correto era {}'.format(x))
