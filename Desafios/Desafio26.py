
# ! Desafio 26
# ! Crie um programa que leia uma frase e mostre quantas vezes aparece a letra "A", 
# ! Em que posiçao ela aparece na primeira veZ, em que posiçao ela aparece na ultima vez

frase = input('Digite uma frase qualquer: ').lower().strip()
#cont = frase.count('a')
posi1 = frase.find('a')
print('A frase digitada possui {} letras A\nA primeira posição é {}\nA ultima posição é {}'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))
   