
# ! Desafio 58
# ! Melhore seu jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10. Só que agora vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessarios para vender.

import random
x = random.randint(0, 5)
cont = 0
num = 99
while num != x:
    print('-=-' * 20)
    num = int(input('Hey você! De 1 a 5, qual numero estou pensando? '))
    print('-=-' * 20)
    cont = cont + 1
    if num == x:
        print('Parabens, você advinhou! Eu estava pensando no numero {}'.format(x))
    else:
        print('ERROU!!! Tente novamente outro numero')
print('Você precisou de {} tentativa(s) para acertar.'.format(cont))
