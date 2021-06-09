
# ! Desafio 48
# ! Crie um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que se encontram no intevalo de 1 até 500.

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1     # ? cont +=1
        s = s + c           # ? s += c
        print(c)
print('A soma de todos os {} numeros acima é {}'.format(cont , s))