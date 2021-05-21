
# ! Desafio 42
# ! Faça um programa que utilize o Desafio35, acrescentando o recurso de mostrar que tipo de triangulo sera formado
# ! Equilatero: todos os lados iguais, Esosceles: dois lados iguais, Escaleno: todos os lados diferentes

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if ((b - c) < a < (b + c)) and ((a - c) < b < (a + c)) and ((a - b) < c < (a + b)):
    print('O triangulo é possivel!')
    if a == b == c:
        print('Triangulo Equilatero')
    elif (a == b or b == c or c == a) and (a != b or b != c or c != a):
        print('Triangulo Isosceles')
    elif a != b or b != c or c != a: # a != b != c != a
        print('Triangulo Escaleno')
else:
    print('Sem triangulo pra você!')