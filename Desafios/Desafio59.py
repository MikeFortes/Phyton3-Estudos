
# ! Desafio 59
# ! Crie um programa que leia dois valores e mostre um menu na tela:
# ![1] Somar
# ![2] Multiplicar
# ![3] Saber o maior valor
# ![4] Novos numeros
# ![5] Sair do programa
# !Seu programa devera realizar a operação solicitada em cada caso
op = ''
print('-=-' * 2, ' ' * 14, 'DIGITE O PRIMEIRO VALOR: ', ' ' * 5, '-=-' * 2)
x = int(input())
print('-=-' * 2, ' ' * 14, 'DIGITE O SEGUNDO VALOR: ', ' ' * 6, '-=-' * 2)
y = int(input())
while op != 5:
    print('-=-' * 20)
    print('-=-' * 2, ' ' * 17, 'CALCULADORA', ' ' * 16, '-=-' * 2)
    print('-=-' * 2, ' ' * 14, 'ESCOLHA 1 OPERAÇÃO', ' ' * 12, '-=-' * 2)
    print('-=-' * 20)
    print('-=-' * 2, ' ' * 2, '[1] - SOMAR', ' ' * 31, '-=-' * 2)
    print('-=-' * 2, ' ' * 2, '[2] - MULTIPLICAR', ' ' * 25, '-=-' * 2)
    print('-=-' * 2, ' ' * 2, '[3] - SABER + VALORES', ' ' * 21, '-=-' * 2)
    print('-=-' * 2, ' ' * 2, '[4] - NOVOS NUMEROS', ' ' * 23, '-=-' * 2)
    print('-=-' * 2, ' ' * 2, '[5] - SAIR', ' ' * 32, '-=-' * 2)
    print('-=-' * 20)
    op = int(input())
    if op == 1:
        r = x + y
        print('{} + {} = {}'.format(x, y, r))
    elif op == 2:
        r = x * y
        print('{} x {} = {}'.format(x, y, r))
print('Finalizando...')
