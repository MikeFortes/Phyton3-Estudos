
# ! Desafio 34
# ! Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para salarios superiores a R$1.250 calcule um aumento de 10%. Para os infeiores ou iguais, o aumento é de 15%.

x = float(input('Digite o seu salario para calculo do reajuste: '))
if x <= 1250:
    y = (15/100) * x
    x = x + y
    print('Seu novo salario sera: R${:.2f}'.format(x))
else:
    y = (10/100) * x
    x = x + y
    print('Seu novo salario sera: R${:.2f}'.format(x))