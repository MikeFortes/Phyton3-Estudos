
# ! Desafio 56
# ! Crie um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# ! A media de idade do grupo
# ! Qual é o nome do homem mais velho
# ! Quantas mulheres tem menos de 20 anos.

listaNome = []
listaIdade = []
listaSexo = []
for p in range(0, 4):
    nome = str(input('Digite seu nome: ')).strip().capitaliz()
    listaNome.append(nome)
    idade = int(input('Digite sua idade: '))
    listaIdade.append(idade)
    sexo = str(input('Digite seu sexo (Masculino, Feminino): ')).strip().capitaliz()
    listaSexo.append(sexo)
media  = sum(listaIdade) / len(listaIdade)
print('A média da idade do grupo é de {} anos'.format(media))
