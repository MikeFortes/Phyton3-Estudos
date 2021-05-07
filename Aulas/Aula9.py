frase = 'Curso em video Python'
# ! O ultimo valor não entra na contagem
print(frase[9:13])

# ! Salta de 2 em 2
print(frase[9:21:2])

# ! Quando omitido o primeiro valor, ele inicia no 0
print(frase[:5])

# ! Quando omitido o ultimo, ele vai ate o final
print(frase[15:])

# ! Vish vei... Vai do 9 até o fim, depois saltar de 3 em 3
print(frase[9::3])

# ! Lens - Comprimento- Qual o comprimento da frase
print(len(frase))

# ! Contador de caracteres
print(frase.count('o'))

# ! Contador de caracteres, ja com fatiamento, ou seja, quantos 'o's dentro do escopo 0-13
print(frase.count('o', 0, 13))