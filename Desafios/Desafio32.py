
# ! Desafio 32
# ! Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
a = int(input('Digite o ano que deseja: '))
if a == 0:
    a = date.today().year
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print('O ano de {} é bissexto!'.format(a))
else:
    print('O ano de {} não é bissexto!'.format(a))