
# ! Desafio 37
# ! Faça um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base da conversão:
# ! 1 para binario, 2 para octal, 3 para hexadecimal

x = int(input('Digite um numero inteiro: '))
opc = int(input('Você deseja converter ele para:\n1 - Binario\n2 - Octal\n3 - Hexadecimal\n'))
# opc = int(input('''Você deseja converter ele para:
# 1 - Binario
# 2 - Octal
# 3 - Hexadecimal'''))
if opc == 1:
    binario = bin(x)
    print('{} convertido em binario é: {}'.format(x, binario[2:]))
elif opc == 2:
    octal = oct(x)
    print('{} convertido em octal é: {}'.format(x, octal[2:]))
elif opc == 3:
    hexa = hex(x)
    print('{} convertido em hexadecimal é: {}'.format(x, hexa[2:]))
else:
    print('A opção escolhida não existe!')