
# ! Desafio 16
# ! Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira

#import math
from math import trunc
num = float(input('Digite um numero qualquer: '))
#print('Valor inteiro: {}'.format(math.trunc(num)))
#print('Valor inteiro: {}'.format(int(num)))
print('Valor inteiro: {}'.format(trunc(num)))