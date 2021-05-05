
# ! Desafio 15
# ! Faça um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcula o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

km = float(input('Quantos quilometros foi percorrido com o carro? '))
d = int(input('Quantos dias você ficou com o carro alugado? '))
kmr = km * 0.15
du = d * 60
t = kmr + du
print('Sua conta ficou em:\n {} Km utilizados = R$ {:.2f}\n {} dias utilizados = R$ {:.2f}\n Total = R$ {:.2f}'.format(km, kmr, d, du, t))rr