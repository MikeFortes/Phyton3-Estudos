
# ! Desafio 24
# ! Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo"

nome = str(input('Digite o nome de sua cidade: '))
nome = nome.split()
pnome = nome[0]
print('Sua cidade começa ou não com a palavra Santo? True or False')
print('Santo' in pnome.capitalize())

# ? Outra forma abaixo com strip, mesmo achando a minha de cima mais bonita coff coff

#cid = str(input('Em que cidade você nasceu? ')).strip()
#print(cid[:5].upper() == 'SANTO')