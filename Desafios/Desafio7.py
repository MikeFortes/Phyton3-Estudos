
# ! Desafio 7
# ! Escreva um programa que leia as duas notas de um aluno, calcule e mostre sua media

x = float(input('Digite sua primeira nota '))
y = float(input('Digite sua segunda nota '))
m = (x + y) / 2
print('A media entre a nota {} e a nota {} é {:.2f}'.format(x, y, m))
