
# ! Desafio 22
# ! Crie um programa que leia o nome completo de uma pessoa e mostre: 
# ! Nome com todas as letras maiusculas
# ! Nome com todas as letras minusculas
# ! Quantas letras o nome possui ao todo (sem contar os espaços)
# ! Quantas letras tem o primeiro nome

nome = str(input('Digita seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome completo possui {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))