import random
from re import I

# Código principal
v = []
for i in range(10):
    v.append(random.randint(10,90))

# a) imprimir vetor
print(v)

# b) Verificar se existe o valor 50 neste vetor (apenas dizer se encontrou ou não)
encontrou = False
for i in v:
    if i == 50:
        encontrou = True
        break
if encontrou == True:
    print('Encontrou o valor 50!')
else:
    print('Não encontrou o valor 50!') 

# c) Verificar o número de ocorrências do valor 50 neste vetor.
cont50 = 0
for i in v:
    if i == 50:
        cont50 += 1
print('Numero de ocorrencias do valor 50: ', cont50)

# d. Calcular a média dos valores do vetor
somatorio = 0
for i in v:
    somatorio += i
media = somatorio/len(v)
print('A media dos valores eh ', media)

# e) Encontrar o maior e o menor valor dos elementos do vetor.
maior = v[0]
menor = v[0]
for i in v:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print('Maior: ', maior)
print('Menor: ', menor)

# f) Imprimir a soma e o produto acumulado dos valores dos elementos do vetor
produtorio = 1
somatorio = 0
for i in v:
    produtorio *= i 
    somatorio += i
print('Somatorio: ', somatorio)
print('Produtorio: ',produtorio)

# g) Imprimir o vetor em ordem inversa
for i in range(1,len(v)+1):
    print(v[-i],end=' ')
print()

# h) Copiar os elementos em ordem inversa para outro vetor.
iv = []
for i in range(1,len(v)+1):
    iv.append(v[-i])
print(iv)

# i) Crie outros dois vetores com 10 elementos, vPares e vImpares. 
# Copie para vPares todos os elementos pares e para vImpares todos os elementos ímpares. 
# Depois disso, imprima o conteúdo de vPares e vImpares.
vPares = []
vImpares = []
for i in v:
    if i % 2 == 0:
        vPares.append(i)
    else:
        vImpares.append(i)
print('Vetor de pares: ', vPares)
print('Vetor de impares: ', vImpares)
