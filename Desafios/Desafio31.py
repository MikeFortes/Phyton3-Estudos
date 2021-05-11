
# ! Desafio 31
# ! Crie um programa que pergunte a distancia de uma viagem em Kms. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

d = float(input('Qual a distancia total percorrida em sua viagem? '))
if d <= 200:
    x = d * 0.50
    print('O valor da sua passagem é de R$ {:.2f}'.format(x))
else:
    x = d * 0.45
    print('O valor da sua passagem é de R$ {:.2f}'.format(x))
    

# ! Simplificado
# x = distancia * 0.50 if d <= 200 else distancia * 0.45
# print('E o preço da sua passagem será de RS{:.2f}'.format(x))