
 # ! Simples
#for c in range(0, 7, 2):
#    print(c)
#print('FIM')

 # ! Simples com variavel final
#n = int(input('Digite um numero: '))
#for c in range (0, n+1):
#    print(c)
#print('FIM')

 # ! Complexo, variavel inicial, final e regra 
#i = int(input('Inicio: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))
#for c in range(i, f+1, p):
#    print(c)
#print('FIM')

s = 0
for c in range (0,4):
    n = int(input('Digite um numero: '))
    s = s + n # ? OU s += n
print('A soma de todas os valores foi: {}'.format(s))