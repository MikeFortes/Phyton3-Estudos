
# ! Desafio 46
# ! Faça um programa que mostre na tela uma contagem regressiva para o estouro dos fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
import emoji
print('-=' * 20)
print('CONTAGEM REGRESSIVA PARA O ANO NOVO !!!')
print('-=' * 20)
for c in range (10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize('FELIZ ANO NOVOO !!! :tada: :tada: :tada:', use_aliases=True))