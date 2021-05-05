
# ! Desafio 8
# ! Escreva um programa que leia um valor em metros e exiba o valor convertido em centimetros e milimetros

x = int(input('Digite um valor em metros '))
cm = x * 100
mm = x * 1000
dm = x * 0.010
hm = x * 0.0100
km = x * 0.01000
print('{} metros convertidos são:\n{} centimetros\n{} milimetros\n{:.2f} decametros\n{:.2f} hectometros\n{:.2f} quilometro'.format(x, cm, mm, dm, hm, km))