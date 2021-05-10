
# ! Desafio 27
# ! Crie um programa que leia o nome completo de uma pessoa e mostre o primeiro e ultimo nome separadamente

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[len(nome)-1]))