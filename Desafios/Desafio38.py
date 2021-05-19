
# ! Desafio 38
# ! Faça um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# ! O primeiro valor é maior, o segundo valor é maior, Não existe valor maior, os dois são iguais.

x = int(input('Digite um numero inteiro: '))
y = int(input('Digite outro numero inteiro: '))
if x > y:
    print('O maior valor é {}'.format(x))
elif y > x:
    print('O maior numero é {}'.format(y))
elif y == x:
    print('Os dois numeros são iguais')