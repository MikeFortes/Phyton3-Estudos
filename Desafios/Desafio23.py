
# ! Desafio 23
# ! Crie um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# ! Exemplo > 1834
# ! Unidades: 4
# ! Dezena: 3
# ! Centena: 8
# ! Milhar: 1

num = input('Digite um numero entre 0 e 9999: ')
print('Unidade: ', num[3:])
print('Dezena: ', num[2:3])
print('Centena: ', num[1:2])
print('Milhar: ', num[:1])