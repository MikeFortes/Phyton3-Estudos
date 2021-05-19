
# ! Condições aninhadas
# ! Uso do elif
# ! Usar quantos "elifs" precisar, porem "else" é apenas um!

nome = str(input('Qual é o seu nome? '))
if nome == 'Michael':
    print('Que nome lindo!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é popular no Brasil...')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino !')
else:
    print('Que nome normal =/')
print('Tenha um bom dia {}'.format(nome))