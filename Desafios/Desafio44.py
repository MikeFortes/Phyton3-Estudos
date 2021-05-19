
# ! Desafio 44
# ! Faça um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
# ! a vista: dinheiro/cheque 10% de desconto, a vista no cartao: 5% de desconto, em até 2x no cartao: preço normal, 3x ou mais no cartao: 20% de juros

x = float(input('Digite o valor pago pelo produto: R$ '))
p = int(input('Escolha o codigo da sua forma de pagamento\n1 - A vista no dinheiro/cheque\n2 - A vista no cartão\n3 - 2x no cartão de credito\n4 - 3x ou mais no cartão de credito\n'))
if p == 1:
    dis = x - ((10/100) * x)
    print('Você recebeu 10% de desconto, o valor a ser pago é R${:.2f}'.format(dis))
if p == 2:
    dis = x - ((5/100) * x)
    print('Você recebeu 5% de desconto, o valor a ser pago é R${:.2f}'.format(dis))
if p == 3:
    print('O valor final sera R${:.2f}'.format(x))
if p == 4:
    acre = x + ((20/100) * x)
    print('Nessa forma de pagamento é aplicado 20% de juros, o valor a ser pago é R${:.2f}'.format(acre))