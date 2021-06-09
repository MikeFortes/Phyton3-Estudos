
# ! Desafio 49
# ! Crie um programa que mostre a tabuada de um numero que o usuario escolher, só que agora utilizando o laço for.


n = int(input('Digite um numero para saber sua tabuada: '))
for c in range (0, 11):
    if c <= 10:
        x = c * n
        print('{} x {:2} = {}'.format(n, c, x))
print('FIM DA TABUADA')