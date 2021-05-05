
# ! Desafio 11
# ! Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua area e a quantidade de tinta necessaria para pintar-la, sabendo que cada litro de tinta pinta uma area de 2m²

l = float(input('Digite a largura da sua parede em metros '))
a = float(input('Digite a altura de sua parede em metros'))
mq = l * a
q = mq / 2
print('Sua parede tem {} metros quadrados é vai utilizar {} litros de tinta para pinta-la'.format(mq , q))