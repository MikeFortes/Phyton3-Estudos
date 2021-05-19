
# ! Desafio 40
# ! Faça um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida.
# ! Media abaixo de 5 : Reprovado, Media entre 5 e 6,9 : Recuperação, Media de 7 ou superior: Aprovado

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Você não atingiu a média esperada, reprovado! Media: {}'.format(m))
elif m >= 5 and m < 6.9:
    print('Você esta de recuperação, Media: {}'.format(m))
elif m > 7:
    print('Você foi aprovado! Media: {}'.format(m))