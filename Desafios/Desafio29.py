
# ! Desafio 29
# ! Crie um programa que leia a velocidade de um carro, se ele ultrapassar 80Kmh mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

v = float(input('Qual a velocidade atual do seu carro? '))
if v <=80:
    print('Muito bem, pode seguir viagem!')
else:
    m = (v - 80) * 7
    print('Você sera multado por excesso de velocidade, pague agora o valor de R$ {:.2f}'.format(m))