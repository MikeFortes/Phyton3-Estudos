
# ! Desafio 10
# ! Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dolares ela pode comprar
# ! Considere US$1,00 = R$3,27

x = float(input('Quantos reais você tem em sua carteira? R$ '))
# ? O valor de Y se trata da cotação do dollar nesse momento
y = 3.27
d = x / y
print(' Voce pode comprar US${:.2f} dolar(es)'.format(d))