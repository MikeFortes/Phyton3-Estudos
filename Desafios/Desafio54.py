
# ! Desafio 54
# ! Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores de idade.
import datetime
atual = datetime.date.today().year
s = 0
con = 0
x = 0
y = 0
for c in range (1, 8):
    n = int(input('Digite o {}º ano de nascimento: '.format(c)))
    if atual - n >= 18:
        x = x + 1
    elif atual - n < 18:
        y = y +1
    s += n
    con += 1
print('{} pessoas são maiores de idade, {} são menores de idade.'.format(x, y))
