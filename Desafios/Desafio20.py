
# ! Desafio 20
# ! Um professor quer sortear a ordem com que os 4 alunos apresentaram seus trabalhos

#import random
from random import shuffle
a = str(input(' Digite o nome do primeiro aluno: '))
b = str(input(' Digite o nome do segundo aluno: '))
c = str(input(' Digite o nome do terceiro aluno: '))
d = str(input(' Digite o nome do quarto aluno: '))
l = [a, b, c, d]
shuffle(l)
print('A ordem de apresentaçao sera esta:\n 1º {}\n 2º {}\n 3º {}\n 4º {}'.format(l[0], l[1], l[2], l[3]))