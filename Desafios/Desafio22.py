
# ! Desafio 22
# ! Crie um programa que leia o nome completo de uma pessoa e mostre: 
# ! Nome com todas as letras maiusculas
# ! Nome com todas as letras minusculas
# ! Quantas letras o nome possui ao todo (sem contar os espaços)
# ! Quantas letras tem o primeiro nome

nomeC = input('Digita seu nome completo: ')
print(nomeC.upper())
print(nomeC.lower())
nomeR = nomeC.replace(' ','')
print(len(nomeR))
nome = nomeC.split()
pnome = nome[0]
print(len(pnome))


