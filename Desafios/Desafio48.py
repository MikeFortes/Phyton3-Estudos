
# ! Desafio 48
# ! Crie um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que se encontram no intevalo de 1 até 500.

s = 0
for c in range(1, 501, 2):
    s = s + c
    print(c)
print('A soma de todos os numeros é {}'.format(s))