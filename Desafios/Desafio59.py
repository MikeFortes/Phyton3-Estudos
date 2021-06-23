
# ! Desafio 59
# ! Crie um programa que leia dois valores e mostre um menu na tela:
# ![1] Somar
# ![2] Multiplicar
# ![3] Saber o maior valor
# ![4] Novos numeros
# ![5] Sair do programa
# !Seu programa devera realizar a operação solicitada em cada caso
op = ''
x = int(input('DIGITE O PRIMEIRO VALOR: '))
y = int(input('DIGITE O SEGUNDO VALOR: '))
while op != 5:
    print('-=-' * 20)
    print('-=-' * 2, ' ' * 14, 'ESCOLHA 1 OPERAÇÃO', ' ' * 12, '-=-' * 2)
    print('-=-' * 20)
    print('[1] - SOMAR')
    print('[2] - MULTIPLICAR')
    print('[3] - SABER O MAIOR VALORE')
    print('[4] - NOVOS NUMEROS')
    print('[5] - SAIR')
    print('-=-' * 20)
    op = int(input())
    if op == 1:
        r = x + y
        print('{} + {} = {}'.format(x, y, r))
    elif op == 2:
        r = x * y
        print('{} x {} = {}'.format(x, y, r))
    elif op == 3:
        if x > y:
            maior = x
            print('{} é o maior numero'.format(x))
        elif y > x:
            maior = y
            print('{} é o maior numero'.format(y))
        else:
            print('Os numeros são iguais!')
    elif op == 4:
        x = int(input('DIGITE O NOVO PRIMEIRO VALOR: '))
        y = int(input('DIGITE O NOVO SEGUNDO VALOR: '))
    else:
        print('Digite uma opção valida.')
print('Finalizando...')
