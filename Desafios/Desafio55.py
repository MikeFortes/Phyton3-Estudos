
# ! Desafio 55
# ! Crie um programa que leia o peso de cinco pessoas. no final mostre qual foi o maior e o menor peso lido.

#lista = []
#for p in range(1, 6):
#    peso = float(input('Digite o {}º peso: '.format(p)))
#    lista.append(peso) # ? ".append" adiciona o valor ao índice.
#print('O maior peso listado é {:.1f}Kg'.format(max(lista)))
#print('O menor peso listado é {:.1f}Kg' .format(min(lista))) 

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o {}º peso: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

