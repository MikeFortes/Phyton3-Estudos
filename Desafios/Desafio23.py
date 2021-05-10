
# ! Desafio 23
# ! Crie um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# ! Exemplo > 1834
# ! Unidades: 4
# ! Dezena: 3
# ! Centena: 8
# ! Milhar: 1

num = int(input('Digite um numero entre 0 e 9999: '))
#n = str(num)
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))

 # ? O formato abaixo aceita unidades vazias, como 0025, enquanto o metodo de cima retorna erro
 
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 100
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))