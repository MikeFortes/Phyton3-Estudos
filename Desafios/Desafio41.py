
# ! Desafio 41
# ! Faça um programa que leia o ano de nascimento de um atleta e mostre sua cateforia de acordo com a idade
# ! Até 9 anos: Mirim, Até 14 anos: Infantil, Até 19 anos: Junior, Até 20 anos: Senior, Acima: Master

import datetime
atual = datetime.date.today().year
print('-=-' * 15)
print('Confederação Brasileira de Desportos Aquaticos')
print('-=-' * 15)
ano = int(input('Para saber sua categoria, digite seu ano de nascimento: '))
x = atual - ano
print('-=-' * 5 ,'Analizando','-=-' * 5)
if x <= 9:
    print('Categoria Mirim')
elif x > 9 and x <= 14:
    print('Cateforia Infantil')
elif x > 14 and x <= 19:
    print('Cateforia Junior')
elif x > 19 and x <= 20:
    print('Cateforia Senior')
elif x > 20:
    print('Cateforia Master')