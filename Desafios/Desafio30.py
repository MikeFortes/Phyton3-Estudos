
# ! Desafio 30
# ! Crie um programa que leia um numero inteiro e mostre se ele é par ou impar

x = int(input('Digite um numero inteiro: '))
if x % 2 == 0:
    print('O numero {} é par!'.format(x))
else:
    print('O numero {} é impar!'.format(x))