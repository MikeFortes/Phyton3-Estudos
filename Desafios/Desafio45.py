
# ! Desafio 45
# ! Faça um programa que faça o computador jogar Jokenpo com você.
import random
# No inicio do programa, o computador ja tem uma escolha definida, independente da escolha do jogador
pc = random.randint(1, 3)
if pc == 1:
    y = 'PEDRA'
elif pc == 2:
    y = 'PAPEL'
elif pc == 3:
    y = 'TESOURA'
print(' --- JoooookeeeeeePO !!! ---')
# Escolha do jogador
x = int(input('Escolha bem!\n1 - PEDRA\n2 - PAPEL\n3 - TESOURA\n'))
if x == 1:
    print('VOCE ESCOLHEU ---PEDRA---')
if x == 2:
    print('VOCE ESCOLHEU ---PAPEL---')
if x == 3:
    print('VOCE ESCOLHEU ---TESOURA---')
print('EU ESCOLHO ---{}---'.format(y))
# Diretriz para escolher vitoria
if (x == 1 and pc == 3) or (pc == 1 and x == 3):
    print('PEDRA GANHA DE TESOURA')
elif (x == 2 and pc == 1) or (pc == 2 and x == 1):
    print('PAPEL GANHA DE PEDRA')
elif (x == 3 and pc == 2) or (pc == 3 and x == 2):
    print('TESOURA GANHA DE PAPEL')
elif x == pc:
    print('EMPATE')