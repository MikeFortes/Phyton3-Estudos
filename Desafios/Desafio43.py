
# ! Desafio 43
# ! Faça um programa que leia o peso e altura de uma pessoa, calcule o IMC e mostre seu Statu, de acordo com a tabela abaixo
# ! Abaixo de 18.5: Abaixo do peso, Entre 18.5 e 25: Peso ideal, 25 até 30: Sobrepeso, 30 até 40: Obesidade, Acima de 40: Obesidade Morbida

from io import IncrementalNewlineDecoder


p = float(input('Digite seu peso em quilos: '))
a = float(input('Digite sua altura em metros: '))
imc = p / (a * a)
print('Seu IMC é: {} Kg/m²'.format(imc))
if imc < 18.5:
    print('Abaixo do peso ideal')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >=30 and imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Morbida')