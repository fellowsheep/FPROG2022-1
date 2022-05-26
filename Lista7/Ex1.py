import random

mat = []
maior = -1
menor = 101
maiori = -1
menori = -1
maiorj = -1
menorj = -1

for i in range(4): #linhas
    aux = [] #lista auxiliar para nova linha
    for j in range(5): #colunas
        nro = random.randint(0,100)
        aux.append(nro) #gera nro e add na lista auxiliar
        if (nro > maior): #testa se é maior
            maior = nro
            maiori = i
            maiorj = j
        if (nro < menor): #testa se é menor
            menor = nro
            menori = i
            menorj = j
    mat.append(aux) #adiciona a linha na matriz

print(mat)
print ('Maior elemento esta em [{}][{}] = {}'.format(maiori,maiorj,maior))
print ('Menor elemento esta em [{}][{}] = {}'.format(menori,menorj,menor))

