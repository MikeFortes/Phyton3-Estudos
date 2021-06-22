
# ! Desafio 57
# ! Crie um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

#sexo = ''
#while sexo.upper() not in {'F', 'M', 'm', 'f'}:
#    sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()
#    if sexo == 'F':
#        sexo = 'Feminino'
#        break
#    elif sexo == 'M':
#        sexo = 'Masculino'
#        break
#    else:
#        print('Escolha uma opção valida: M para Masculino ou F para Feminino')    
#print('Seu sexo é {}'.format(sexo))
#print('Fim')

# ? Forma ensinada na aula ABAIXO

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Invalidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
if sexo == 'F':
    sexo = 'Feminino'
if sexo == 'M':
    sexo = 'Masculino'
print('Sexo {} registrado com sucesso!'.format(sexo))
