
# ! Desafio 57
# ! Crie um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo.upper() not in {'F', 'M'}:
    sexo = str(input('Digite seu sexo: [M/F]')).strip()
if sexo == 'F':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'    
print('Seu sexo é {}'.format(sexo))
print('Fim')