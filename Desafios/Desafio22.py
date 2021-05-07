
# ! Desafio 22
# ! Crie um programa que leia o nome completo de uma pessoa e mostre: 
# ! Nome com todas maiusculas
# ! Nome com todas minusculas
# ! Quantas letras ao todo(sem contar os espaços)
# ! Quantas letras tem o primeiro nome

nome = str(input('Digita seu nome completo: '))
print(nome.upper())
print(nome.lower())
nome = nome.split()
pnome = nome[0]
print(pnome)
print(len(pnome))
