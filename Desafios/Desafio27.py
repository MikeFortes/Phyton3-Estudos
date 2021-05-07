
# ! Desafio 27
# ! Crie um programa que leia o nome completo de uma pessoa e mostre o primeiro e ultimo nome separadamente

nome = input('Digite seu nome completo:')
nome = nome.split()
x = len(nome) - 1
pri = nome[0]
ult = nome[x]
print('Primenri nome: ', pri)
print('Ultimo nome: ', ult)