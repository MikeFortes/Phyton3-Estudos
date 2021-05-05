
# ! Desafio 12
# ! Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

po = int(input('Digite o valor do produto '))
pa = (5/100) * po
x = po - pa
print('O valor com 5% de desconto é: {}'.format(x))