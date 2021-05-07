
# ! Desafio 26
# ! Crie um programa que leia uma frase e mostre quantas vezes aparece a letra "A", 
# ! Em que posiçao ela aparece na primeira veZ, em que posiçao ela aparece na ultima vez

frase = input('Digite uma frase qualquer: ')
cont = frase.count('a')
posi = frase.find('a')
print('A frase digitada possui {} letras a nas posições {}'.format(cont, posi))
