
# ! Desafio 58
# ! Melhore seu jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10. Só que agora vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessarios para vender.

#import random
#x = random.randint(0, 10)
#cont = 0
#num = 99
#while num != x:
#    print('-=-' * 20)
#    num = int(input('Hey você! De 1 a 5, qual numero estou pensando? '))
#    print('-=-' * 20)
#    cont = cont + 1
#    if num == x:
#        print('Parabens, você advinhou! Eu estava pensando no numero {}'.format(x))
#    else:
#        print('ERROU!!! Tente novamente outro numero')
#print('Você precisou de {} tentativa(s) para acertar.'.format(cont))

# ? Forma ensinada na aula ABAIXO

import random
x = random.randint(0, 10)
print('-=-' * 20)
print('Vamos brincar de advinha? Vou escolher um numero entre 0 e 10.')
print('Será que voce consegue advinhar qual foi???')
print('-=-' * 20)
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Qual o seu palpite??? '))
    cont = cont + 1 # ? cont += 1
    if jogador == x:
        acertou = True
    else:
        if jogador < x:
            print('Mais... Tente mais uma vez!')
        elif jogador > x:
            print('Menos... Tente novamente!')
print('Acertou!!! Pensei no numero {}! Você precisou de {} tentativas'.format(x, cont))
