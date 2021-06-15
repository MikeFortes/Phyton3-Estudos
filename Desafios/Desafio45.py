
# ! Desafio 45
# ! Faça um programa que faça o computador jogar Jokenpo com você.
from random import randint
from time import sleep
# No inicio do programa, o computador ja tem uma escolha definida, independente da escolha do jogador
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
# Escolha do jogador
print('''Suas opções:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')
x = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
print('-=' * 12)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[x]))
print('-=' * 12)

if pc == 0: # Computador jogou Pedra
    if x == 0: # Jogador jogou Pedra
        print('EMPATE')
    elif x == 1: # Jogador jogou Papel
        print('JOGADOR VENCE')
    elif x == 2: # Jogador jogou Tesoura
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA') 
elif pc == 1: # Computador jogou Papel
    if x == 0: # Jogador jogou Pedra
        print('COMPUTADOR VENCE')
    elif x == 1: # Jogador jogou Papel
        print('EMPATE')
    elif x == 2: # Jogador jogou Tesoura
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA') 
elif pc == 2: # Computador jogou Tesoura
    if x == 0: # Jogador jogou Pedra
        print('JOGADOR VENCE')
    elif x == 1: # Jogador jogou Papel
        print('COMPUTADOR VENCE')
    elif x == 2: # Jogador jogou Tesoura
        print('EMPATE')
