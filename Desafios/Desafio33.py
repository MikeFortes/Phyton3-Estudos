
# ! Desafio 33
# ! Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor

x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))
z = int(input('Digite o terceiro numero: '))

# Achando o maior numero
maior = x
if (y > maior):
    maior = y
if (z > maior):
    maior = z
    
print('Maior: ', maior)

# Achando o numero menor
menor = x
if (y < menor):
    menor = y
if (z < menor):
    menor = z

print('Menor: ', menor)