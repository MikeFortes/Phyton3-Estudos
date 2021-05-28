
# ! Desafio 51
# ! Crie um programa que leia o primeiro termo e a razao de uma PA (Progressão Aritmetica). No final, mostre os 10 primeiros termos dessa progressão.

p1 = int(input("Primeiro termo: ") )
r = int(input("Razao: ") )
n = 10

x = p1 + (n-1)*r
x = x + 1

for var in range(p1, x, r):
    print(var)