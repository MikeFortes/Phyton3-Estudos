
# ! Desafio 31
# ! Crie um programa que pergunte a distancia de uma viagem em Kms. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,40 para viagens mais longas.

d = float(input('Qual a distancia total percorrida em sua viagem? '))
if d <= 200:
    x = d * 0.40
    print('O valor da sua passagem é de R$ {:.2f}'.format(x))
else:
    x = d * 0.50
    print('O valor da sua passagem é de R$ {:.2f}'.format(x))