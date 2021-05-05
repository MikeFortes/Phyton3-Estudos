
# ! Desafio 18
# ! Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

import math

a = float(input("Digite o ângulo que você deseja: "))
print("Seno: {:.2f}".format(math.sin(math.radians(a))))
print("Cosseno: {:.2f}".format(math.cos(math.radians(a))))
print("Tangente: {:.2f}".format(math.tan(math.radians(a))))

#print('Os valores são:\n Seno {}°\n Cosseno {}°\n Tangente {}°'.format(math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))