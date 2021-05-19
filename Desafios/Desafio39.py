
# ! Desafio 39
# ! Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# ! Se ele ainda vai se alistar ao serviço militar, Se é a hora de se alistar, Se ja passou do tempo do alistamento.
# ! Informar tambem quanto tempo falta ou que passou do prazo.
import datetime
atual = datetime.date.today().year
ano = int(input('Digite o ano de seu nascimento: '))
x = atual - ano # Quantos anos a pessoa tem 
if x < 18:
    y = 18 - x
    print('Você ainda não tem idade para se alistar, {} anos restantes'.format(y))
elif x == 18:
    print('Você deve se alistar este ano!')
elif x > 19:
    y = x - 18
    print('Você ja devia ter se alistado! Esta {} anos atrasado!'.format(y))