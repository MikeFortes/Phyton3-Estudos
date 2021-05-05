
# ! Desafio 17
# ! Faça um programa que leia o comprimento do cateto oposto e do caceto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

# ? a² + b² = C²

from math import hypot
#import math
co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))
hip = math.hypot(co, ca)
#hip = (ca ** 2 + co ** 2) ** (1/2)
print('O valor da hipotenusa é: {}'.format(hip))

