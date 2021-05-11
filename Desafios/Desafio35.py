
# ! Desafio 35
# ! Faça um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo.

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if ((b - c) < a < (b + c)) and ((a - c) < b < (a + c)) and ((a - b) < c < (a + b)):
    print('O triangulo é possivel!')
else:
    print('Sem triangulo pra você!')