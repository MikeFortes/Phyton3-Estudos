
# ! Desafio 4
# ! Crie um programa que leia algo do teclado e mostra seu tipo primitico e todas informaçoes sobre ele

x = input('Digite algo no teclado \n')
print('O tipo primitivo desse valor é: ', type(x))
print(x, 'é numerico? ', x.isnumeric())
print(x, 'é alfabetico? ', x.isalpha())
print(x, 'Só tem espaços? ', x.isspace())
print(x, 'é alfanumerico? ', x.isalnum())
print(x, 'tem letras maiusculas? ', x.isupper())
print(x, 'tem letras minusculas? ', x.islower())
print(x, 'esta capitalizado? ', x.istitle())