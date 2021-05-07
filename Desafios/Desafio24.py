
# ! Desafio 24
# ! Crie um programa que leia o nome de uma cidade e dia se ela começa ou nao com o nome "SANTO"

nome = str(input('Digite o nome de sua cidade: '))
nome = nome.split()
pnome = nome[0]
print('Sua cidade começa ou não com a palavra Santo? True or False')
print('Santo' in pnome)