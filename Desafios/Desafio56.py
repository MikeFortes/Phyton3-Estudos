
# ! Desafio 56
# ! Crie um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# ! A media de idade do grupo
# ! Qual é o nome do homem mais velho
# ! Quantas mulheres tem menos de 20 anos.

SomaIdade = 0
MediaIdade = 0
MaiorIdade = 0
NomeVelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('---- {} º PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    SomaIdade += idade
    if p == 1 and sexo in 'Mm':
        MaiorIdade = idade
        NomeVelho = nome
    if sexo in 'Mm' and idade > MaiorIdade:
        MaiorIdade = idade
        NomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 +=1
MediaIdade = SomaIdade / 4
print('----- Calculando -----')
print('A média de idade do grupo é de {} anos'.format(MediaIdade))
print('O homem mais velho é o {} com {} anos de idade'.format(NomeVelho, MaiorIdade))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))