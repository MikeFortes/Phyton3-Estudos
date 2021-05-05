
# ! Desafio 6
# ! Crie um programa que leia um numero e mostre o dobro, triplo e raiz quadrada

n = int(input('Digite um numero qualquer '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro do valor digitado é {}, o triplo é {} e a raiz quadrada de {} é {:.2f}'.format(d, t, n, r))