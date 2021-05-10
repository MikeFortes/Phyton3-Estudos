
# ! Condição if else

#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo<=3:
#    print('Carro novo')
#else:
#    print('Carro velho')
#print('--FIM--')

# ? Condição simplificada

#tempo = int(input('Quantos anos tem seu carro? '))
#print('Carro novo' if tempo<=3 else 'Carro velho')
#print('--FIM--')

# ! Outro exemplo

#nome = str(input('Qual o seu nome? '))
#if nome == 'Michael':
#    print('Que nome lindo você tem!!! ')
#else:
#    print('Seu nome é meio zuado')
#print('Bom dia {}'.format(nome))

# ! Media de nota, recuperação

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >=6:
    print('Sua média foi {}\nVocê passou de ano, parabens !!!'.format(m))
else:
    print('Sua média foi {}\nReprovado fracassado =/'.format(m)) 
    
 # ? Condição simplificada
#print('Parabens' if m >=6 else 'Reprovado')