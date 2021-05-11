
# ! Desafio 32
# ! Faça um programa que leia um ano qualquer e mostre se ele é bissexto

a = int(input('Digite o ano que deseja: '))
if (a%4==0 and a%100!=0) or (a%400==0):
    print('O {} ano é bissexto!'.format(a))
else:
    print('{} não é bissexto!'.format(a))