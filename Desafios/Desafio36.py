
# ! Desafio 36
# ! Faça um programa que aprove um emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salario ou então o emprestimo será negado.

print('Ola querido cliente! Para validarmos seu emprestimo, precisamos saber de algumas informações.')
valor = float(input('Qual o valor da casa que você pretende comprar? R$ '))
salario = float(input('Qual o seu salario? R$ '))
tempo = int(input('Em quantos meses você pretende pagar esse imovel por completo? '))
prestacao = valor / (tempo * 12) # 12 meses - 1 ano
x = (30/100) * salario
if prestacao > x:
    print('As prestações ultrapassam 30% do seu salario, emprestimo negado')
else:
    print('Emprestimo aprovado!!!')






